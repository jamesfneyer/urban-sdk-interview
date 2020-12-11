import os

from flask import Flask
from flask_rest_jsonapi import Api


def create_flask_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=f'postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}'
                                f'@{os.environ["POSTGRES_URL"]}/{os.environ["POSTGRES_DB"]}'
    )

    from .db import db, migrate

    app.config.from_json('../config.json')
    db.init_app(app)
    migrate.init_app(app, db)

    from .views import IncidentsList, IncidentsDetail
    api = Api(app)
    api.route(IncidentsList, 'incidents_list', '/incidents')
    api.route(IncidentsDetail, 'incidents_detail', '/incidents/<int:id>')

    return app
