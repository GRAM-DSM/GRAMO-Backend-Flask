from flask import abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token

import random

from server.model import Session, Redis
from server.model.user import User
from server.controller.email import send_email


def sign_up(email, password, name, major):
    add_user = User(email=email, password=generate_password_hash(password), name=name, major=major, email_status=1)
    Session.add(add_user)
    Session.commit()

    return 201


def send_email_code(email):
    user = Session.query(User).filter(User.email == email).first()

    if user:
        return abort(409, 'this email is already in use')

    code = f"{random.randint(111111, 999999):04d}"
    title = "GRAMO 이메일 인증 메일"
    content = f"이메일 인증 코드는 {code}입니다."

    send_email(title=title, content=content, adress=email)

    # redis에 이메일코드 저장
    Redis.setex(name=email, value=code, time=180)

    return 200


def check_code(email, code):
    # redis에서 이메일코드 가져옴
    user = Redis.get(email)

    if not user:
        return abort(404, 'this email does not exist')

    if user.code != code:
        return abort(400, 'email and code does not match')

    return 200


def login(email, password):
    user = Session.query(User).filter(User.email == email).first()

    if not user:
        return abort(404, 'could not find account matching this email')

    check_user_pw = check_password_hash(user.password, password)

    if check_user_pw:
        access_token = create_access_token(identity=email)
        refresh_token = create_refresh_token(identity=email)

        # redis에 refresh 토큰 저장
        Redis.setex(name=email, value=refresh_token, time=3600)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }, 201

    else:
        return abort(404, 'email and password does not match')


def token_refresh(email):
    access_token = create_access_token(identity=email)

    return {
        "access_token": access_token
    }, 201


# 구현
def logout(email):
    # redis에서 사용자 가져옴
    user = Redis.get(email)

    if user:
        # refresh 토큰 삭제
        Redis.delete(email)

        return 204

    else:
        return abort(401, 'could not find token user')
