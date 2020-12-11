from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from geoalchemy2 import Geometry

db = SQLAlchemy()
migrate = Migrate()


class Incidents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    county_name = db.Column(db.String(50), nullable=False)

    location = db.Column(Geometry('POINT', srid=4326), nullable=False)
    shape = db.Column(Geometry('MULTIPOLYGON', srid=4326), nullable=False)
