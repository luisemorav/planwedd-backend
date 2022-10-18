from app import api
from flask import request
from flask_restx import Resource
from app.schemas.roles_schema import RolesRequestSchema
from app.controllers.roles_controller import RolesController
from flask_jwt_extended import jwt_required

role_ns = api.namespace(
    name='Roles',
    description='Rutas del modulo Roles',
    path='/roles'
)

request_schema = RolesRequestSchema(role_ns)


@role_ns.route('')
@role_ns.doc(security='Bearer')
class Roles(Resource):
    @jwt_required()
    def get(self):
        ''' Listar todos los roles '''
        controller = RolesController()
        return controller.all()

    @jwt_required()
    @role_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creación de roles '''
        controller = RolesController()
        return controller.create(request.json)


@role_ns.route('/<int:id>')
@role_ns.doc(security='Bearer')
class RoleById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener un rol por el ID '''
        controller = RolesController()
        return controller.getById(id)

    @jwt_required()
    @role_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar un rol por el ID '''
        controller = RolesController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar un rol por el ID '''
        controller = RolesController()
        return controller.delete(id)


api.add_namespace(role_ns)
