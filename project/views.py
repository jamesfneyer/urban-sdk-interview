from flask_rest_jsonapi import ResourceList, ResourceDetail

from .db import Incidents, db
from .schemas import IncidentSchema


class IncidentsDetail(ResourceDetail):
    schema = IncidentSchema
    data_layer = {
        'session': db.session,
        'model': Incidents
    }


class IncidentsList(ResourceList):
    schema = IncidentSchema
    data_layer = {'session': db.session, 'model': Incidents}

