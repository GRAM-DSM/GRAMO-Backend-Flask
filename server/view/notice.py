from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from server.controller.notice import create_notice, get_notice_list, delete_notice, get_detail_notice
from server.view import validate_JSON
from server.model.validator import CreateNoticeValidator


class CreateNotice(Resource):

    @jwt_required()
    @validate_JSON(CreateNoticeValidator)
    def post(self):
        title = request.json['title']
        content = request.json['content']

        user_email = get_jwt_identity()

        return create_notice(title=title,
                             content=content,
                             user_email=user_email)


class GetNotice(Resource):

    @jwt_required()
    def get(self, page):

        return get_notice_list(page=page)


class SpecificNotice(Resource):

    @jwt_required()
    def delete(self, notice_id):
        user_email = get_jwt_identity()

        return delete_notice(notice_id=notice_id,
                             user_email=user_email)

    @jwt_required()
    def get(self, notice_id):
        return get_detail_notice(notice_id=notice_id)
