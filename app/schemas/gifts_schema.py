from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.gifts_model import GiftModel
from flask_restx.reqparse import RequestParser


class GiftsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        return self.namespace.model('Gift Create', {
            'nombre': fields.String(required=True, min_length=2, max_length=100),
            'descripcion': fields.String(required=False, max_length=300),
            'img_regalo': fields.String(required=False, max_length=100),
            'precio': fields.String(required=False, max_length=12),
            'evento_id': fields.Integer(required=True)
        })

    def update(self):
        return self.namespace.model('Gift Update', {
            'nombre': fields.String(required=False, max_length=100),
            'descripcion': fields.String(required=False, max_length=300),
            'img_regalo': fields.String(required=False, max_length=100),
            'precio': fields.String(required=False, max_length=12),
        })


class GiftsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GiftModel
        ordered = True

    evento = Nested('EventsResponseSchema', exclude=['regalos', 'usuario', 'dedicatorias'], many=False)
