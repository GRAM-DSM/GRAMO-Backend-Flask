from flask_jwt_extended import JWTManager

from server.model import Base, engine
from server import create_app

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app = create_app()
    jwt = JWTManager(app)
    app.run(host="0.0.0.0", debug=True)
