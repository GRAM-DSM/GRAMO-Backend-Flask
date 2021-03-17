from server.model import Base, engine
from server import create_app

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app = create_app()
    app.run(debug=True)
