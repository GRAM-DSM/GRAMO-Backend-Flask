from flask import abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

import random

from server.model import session, Redis
from server.model.user import User
from server.controller.email import send_email


def sign_up(email, password, name, major):
    origin_user = session.query(User).filter(User.email == email).first()

    if origin_user:
        abort(409, "this email is already in use")
    else:
        add_user = User(email=email,
                        password=generate_password_hash(password),
                        name=name, major=major,
                        email_status=1)
        session.add(add_user)
        session.commit()

        return 201


def send_email_code(email):
    user = session.query(User).filter(User.email == email).first()

    if user:
        abort(409, 'this email is already in use')

    code = f"{random.randint(111111, 999999):04d}"
    title = "GRAMO 이메일 인증 메일"
    content = f"이메일 인증 코드는 {code}입니다."

    send_email(title=title,
               content=content,
               adress=email)

    Redis.setex(name=email,
                value=code,
                time=180)

    return 200


def check_code(email, code):
    stored_code = int(Redis.get(email))

    if not stored_code:
        abort(404, 'this email does not exist')

    if stored_code != code:
        abort(409, 'email and code does not match')

    return 200


def login(email, password):
    user = session.query(User).filter(User.email == email).first()

    check_user_pw = check_password_hash(user.password, password)

    if check_user_pw:
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)

        Redis.setex(name=email,
                    value=refresh_token,
                    time=604800)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }, 201

    else:
        abort(404, 'email and password does not match')


def token_refresh(email):
    access_token = create_access_token(identity=email)

    return {
        "access_token": access_token
    }, 201


def logout(email):
    token = Redis.get(email)

    if token:
        Redis.delete(email)

        return 204

    else:
        abort(401, 'could not find token user')
