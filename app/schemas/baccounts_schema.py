from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.baccounts_model import BaccountModel
from flask_restx.reqparse import RequestParser


class BaccountsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=5, location='args')
        return parser

    def create(self):
        return self.namespace.model('Baccount Create', {
            'banco': fields.String(required=False, max_length=60, default="Sin asignar"),
            'nro_cuenta': fields.String(required=False, max_length=50, default=""),
            'titular': fields.String(required=False, max_length=100, default=""),
            'usuario_id': fields.Integer(required=True)
        })

    def update(self):
        return self.namespace.model('Baccount Update', {
            'banco': fields.String(required=False, max_length=60),
            'nro_cuenta': fields.String(required=False, max_length=50),
            'titular': fields.String(required=False, max_length=100),
        })


class BaccountsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BaccountModel
        ordered = True

    usuario = Nested('UsersResponseSchema', exclude=['cuentas', 'eventos'], many=False)
