from flask import Flask

from server.router import bp

from server.config import SECRET_KEY, ACCESS_TIMEOUT, REFRESH_TIMEOUT


def create_app():
    _app = Flask(__name__)

    _app.secret_key = SECRET_KEY
    _app.config['JWT_ACCESS_TOKEN_EXPIRES'] = ACCESS_TIMEOUT
    _app.config['JWT_REFRESH_TOKEN_EXPIRES'] = REFRESH_TIMEOUT

    _app.register_blueprint(bp)

    return _app
