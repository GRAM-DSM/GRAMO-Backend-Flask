from flask import request, abort
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.controller.auth import sign_up, send_email_code, check_code, login, logout, token_refresh
from server.controller.form import SignupForm


class SignUp(Resource):
    def post(self):
        # email = request.json['email']
        # password = request.json['password']
        # name = request.json['name']
        # major = request.json['major']

        form = SignupForm()
        if form.validate():
            return sign_up(email=form.email.data, password=form.password.data,
                           name=form.name.data, major=form.major.data)
        return abort(400, 'bad request')

    def get(self):
        email = request.json['email']

        return send_email_code(email=email)

    def put(self):
        email = request.json['email']
        code = request.json['code']

        return check_code(email=email, code=code)


class Auth(Resource):
    def post(self):
        email = request.json['email']
        password = request.json['password']

        return login(email=email, password=password)

    @jwt_required(refresh=True)
    def put(self):
        email = get_jwt_identity()

        return token_refresh(email)

    @jwt_required
    def delete(self):
        email = get_jwt_identity()

        return logout(email=email)
