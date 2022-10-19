from flask_restx import fields
# from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.gifts_model import GiftModel
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage

class GiftsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=10, location='args')
        return parser

    def create(self):
        parser = RequestParser()
        parser.add_argument('nombre', type=str, required=True, location='form')
        parser.add_argument('descripcion', type=str, required=False, location='form')
        parser.add_argument('img_regalo', type=FileStorage, required=False, location='files')
        parser.add_argument('precio', type=str, required=False, location='form')
        parser.add_argument('evento_id', type=int, required=True, location='form')

        return parser
        # return self.namespace.model('Gift Create', {
        #     'nombre': fields.String(required=True, min_length=2, max_length=100),
        #     'descripcion': fields.String(required=False, max_length=300),
        #     'img_regalo': fields.String(required=False, max_length=100),
        #     'precio': fields.String(required=False, max_length=12),
        #     'evento_id': fields.Integer(required=True)
        # })

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
        include_fk = True

    # evento = Nested('EventsResponseSchema', exclude=['regalos', 'dedicatorias'], many=False)
