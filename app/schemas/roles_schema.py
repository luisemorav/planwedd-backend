from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.roles_model import RoleModel


class RolesRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Role Create', {
            'name': fields.String(required=True, max_length=120)
        })

    def update(self):
        return self.namespace.model('Role Update', {
            'name': fields.String(required=True, max_length=120)
        })


class RolesResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RoleModel
        ordered = True

    usuarios = Nested('UsersResponseSchema', exclude=['rol', 'eventos'], many=True)
