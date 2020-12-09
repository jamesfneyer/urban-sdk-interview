import enum

from sqlalchemy import Column, DateTime, Enum, Integer, String
from geoalchemy2 import Geometry
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Incident(db.Model):
    class Counties(str, enum.Enum):
        PUTNAM = 'PUTNAM'
        TAYLOR = 'TAYLOR'
        OKALOOSA = 'OKALOOSA'

    id = db.Column(Integer, primary_key=True)
    description = Column(String(255))
    datetime = Column(DateTime)
    county_name = Column(Enum(Counties))

    location = Column(Geometry('POINT'))
    shape = Column(Geometry('MULTIPOLYGON'))
