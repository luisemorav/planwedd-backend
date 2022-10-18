from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.users_model import UserModel
from flask_restx.reqparse import RequestParser


class UsersRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def all(self):
        parser = RequestParser()
        parser.add_argument('page', type=int, default=1, location='args')
        parser.add_argument('per_page', type=int, default=5, location='args')
        return parser

    def create(self):
        return self.namespace.model('User Create', {
            'nombres': fields.String(required=True, min_length=2, max_length=120),
            'apellidos': fields.String(required=True, min_length=2, max_length=160),
            'dni': fields.String(required=True, max_length=8),
            'username': fields.String(required=True, min_length=2, max_length=80),
            'password': fields.String(required=True, min_length=5, max_length=120),
            'img': fields.String(required=False, max_length=160),
            'correo': fields.String(required=True, min_length=3, max_length=120),
            'rol_id': fields.Integer(readonly=True, default=2)
        })

    def update(self):
        return self.namespace.model('User Update', {
            'nombres': fields.String(required=False, max_length=120),
            'apellidos': fields.String(required=False, max_length=160),
            'dni': fields.String(required=False, max_length=8),
            'username': fields.String(required=False, max_length=80),
            'password': fields.String(required=False, max_length=120),
            'img': fields.String(required=False, max_length=160),
            'correo': fields.String(required=False, max_length=120),
        })


class UsersResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = UserModel
        ordered = True
        exclude = ['password']

    rol = Nested('RolesResponseSchema', exclude=['usuarios'], many=False)
    eventos = Nested('EventsResponseSchema', exclude=['usuario', 'regalos', 'dedicatorias'], many=True)
    cuentas = Nested('BaccountsResponseSchema', exclude=['usuario'], many=True)
