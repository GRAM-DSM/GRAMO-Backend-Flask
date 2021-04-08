from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.controller.auth import sign_up, send_email_code, check_code, login, logout, token_refresh
from server.view import validate_JSON
from server.model.validator import SignupValidator, SigninValidator


class SignUp(Resource):
    @validate_JSON(SignupValidator)
    def post(self):
        email = request.json['email']
        password = request.json['password']
        name = request.json['name']
        major = request.json['major']

        return sign_up(email=email, password=password, name=name, major=major)


class SendEmail(Resource):
    def post(self):
        email = request.json['email']

        return send_email_code(email=email)


class CheckEmailCode(Resource):
    def post(self):
        email = request.json['email']
        code = request.json['code']

        return check_code(email=email, code=code)


class Auth(Resource):
    @validate_JSON(SigninValidator)
    def post(self):
        email = request.json['email']
        password = request.json['password']

        return login(email=email, password=password)

    @jwt_required(refresh=True)
    def get(self):
        email = get_jwt_identity()

        return token_refresh(email)

    @jwt_required()
    def delete(self):
        email = get_jwt_identity()

        return logout(email=email)
