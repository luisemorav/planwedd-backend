from flask_restx import fields
# from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.events_model import EventModel
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage


class EventsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        parser = RequestParser()
        parser.add_argument('nombre_evento', type=str, required=True, location='form')
        parser.add_argument('fecha_evento', type=str, required=False, location='form')
        parser.add_argument('texto_portada', type=str, required=False, location='form')
        parser.add_argument('img_portada', type=FileStorage, required=False, location='files')
        parser.add_argument('configuraciones', type=str, required=True, location='form')

        return parser
        # return self.namespace.model('Event Create', {
        #     'nombre_evento': fields.String(required=True, min_length=2, max_length=200),
        #     'fecha_evento': fields.String(required=False, min_length=10, max_length=15, default="dd/mm/aaaa"),
        #     'texto_portada': fields.String(required=False, max_length=300, default="Escribe tu bienvenida aquí"),
        #     'img_portada': fields.String(required=False),
        #     'configuraciones': fields.String(required=False),
        #     'usuario_id': fields.Integer(required=True)
        # })

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
        include_fk = True
    # usuario = Nested('UsersResponseSchema', exclude=['eventos', 'rol'], many=False)
    # regalos = Nested('GiftsResponseSchema', exclude=['evento'], many=True)
    # dedicatorias = Nested('GiftsResponseSchema', exclude=['evento'], many=True)
