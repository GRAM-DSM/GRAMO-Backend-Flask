from flask import Blueprint
from flask_restful import Api

bp = Blueprint("post", __name__, url_prefix="")
api_basic = Api(bp)

# url 미정
from server.view.auth import SignUp
api_basic.add_resource(SignUp, "/email")

from server.view.auth import Auth
api_basic.add_resource(Auth, "/auth")

from server.view.notice import GeneralNotice
api_basic.add_resource(GeneralNotice, "/notice")

from server.view.notice import SpecificNotice
api_basic.add_resource(SpecificNotice, "/notice/<int:notice_id>")
