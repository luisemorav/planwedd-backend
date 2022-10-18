from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.dedications_model import DedicationModel
from flask_restx.reqparse import RequestParser

class DedicationsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        return self.namespace.model('Dedication Create', {
            'nombre': fields.String(required=True, min_length=2, max_length=120),
            'contenido': fields.String(required=True, max_length=400),
            'evento_id': fields.Integer(required=True)
        })

    def update(self):
        return self.namespace.model('Dedicaton Update', {
            'nombre': fields.String(required=False, max_length=120),
            'contenido': fields.String(required=False, max_length=400),
        })


class DedicationsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = DedicationModel
        ordered = True

    evento = Nested('EventsResponseSchema', exclude=['dedicatorias', 'regalos', 'usuario'], many=False)
