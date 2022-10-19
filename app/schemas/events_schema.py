from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.events_model import EventModel
from flask_restx.reqparse import RequestParser


class EventsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        return self.namespace.model('Event Create', {
            'nombre_evento': fields.String(required=True, min_length=2, max_length=200),
            'fecha_evento': fields.String(required=False, min_length=10, max_length=15),
            'texto_portada': fields.String(required=False, max_length=300),
            'img_portada': fields.String(required=False),
            'configuraciones': fields.String(required=False),
            'usuario_id': fields.Integer(required=True)
        })

    def update(self):
        return self.namespace.model('Event Update', {
            'nombre_evento': fields.String(required=False, max_length=200),
            'fecha_evento': fields.String(required=False, max_length=15),
            'texto_portada': fields.String(required=False, max_length=300),
            'img_portada': fields.String(required=False),
            'configuraciones': fields.String(required=False),
        })


class EventsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = EventModel
        ordered = True

    # usuario = Nested('UsersResponseSchema', exclude=['eventos', 'rol'], many=False)
    regalos = Nested('GiftsResponseSchema', exclude=['evento'], many=True)
    dedicatorias = Nested('GiftsResponseSchema', exclude=['evento'], many=True)
