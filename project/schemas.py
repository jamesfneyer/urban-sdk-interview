from geoalchemy2.shape import to_shape
from marshmallow_jsonapi import fields
from marshmallow_jsonapi.flask import Schema
from shapely import geometry

from .db import Incidents


def to_geojson(collection):
    return geometry.mapping(to_shape(collection))


class IncidentSchema(Schema):
    id = fields.Integer(as_string=True)
    description = fields.String()
    datetime = fields.DateTime()
    county_name = fields.String()

    location = fields.Function(lambda obj: to_geojson(obj.location))
    shape = fields.Function(lambda obj: to_geojson(obj.shape))

    class Meta:
        type_ = 'incident'
        self_view = 'incidents_detail'
        self_view_kwargs = {'id': '<id>'}
        model = Incidents
