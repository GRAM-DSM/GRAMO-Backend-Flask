from flask import Flask

from server.router import bp

from server.config import SECRET_KEY


def create_app():
    _app = Flask(__name__)

    _app.secret_key = SECRET_KEY
    _app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400
    _app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 604800

    _app.register_blueprint(bp)

    return _app
