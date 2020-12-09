import os

from flask import Flask
from flask_migrate import Migrate


def create_flask_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=f'postgis://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}'
                                f'@psql/{os.environ["POSTGRES_USER"]}'
    )

    from .model import Incident

    app.config.from_json('config.json', silent=True)
    SQLAlchemy().init_app(app)
    Migrate().init_app(app, Incident)

    return app
