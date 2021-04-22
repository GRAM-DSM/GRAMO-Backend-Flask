from flask import Blueprint
from flask_restful import Api

bp = Blueprint("gramo", __name__, url_prefix="")
api_basic = Api(bp)

from server.view.auth import SignUp
api_basic.add_resource(SignUp, "/signup")

from server.view.auth import SendEmail
api_basic.add_resource(SendEmail, "/sendemail")

from server.view.auth import CheckEmailCode
api_basic.add_resource(CheckEmailCode, "/checkcode")

from server.view.auth import Auth
api_basic.add_resource(Auth, "/auth")

from server.view.auth import Withdrawal
api_basic.add_resource(Withdrawal, "/withdrawal")

from server.view.notice import CreateNotice
api_basic.add_resource(CreateNotice, "/notice")

from server.view.notice import GetNotice
api_basic.add_resource(GetNotice, "/notice/<int:off_set>/<int:limit_num>")

from server.view.notice import SpecificNotice
api_basic.add_resource(SpecificNotice, "/notice/<int:notice_id>")
