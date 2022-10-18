from app import api
from flask import request
from flask_restx import Resource
from app.schemas.users_schema import UsersRequestSchema
from app.controllers.users_controller import UsersController
from flask_jwt_extended import jwt_required

user_ns = api.namespace(
    name='Usuarios',
    description='Rutas del modulo Usuarios',
    path='/users'
)

request_schema = UsersRequestSchema(user_ns)


@user_ns.route('')
@user_ns.doc(security='Bearer')
class Users(Resource):
    @jwt_required()
    @user_ns.expect(request_schema.all())
    def get(self):
        ''' Listar todos los usuarios '''
        query_params = request_schema.all().parse_args()
        controller = UsersController()
        return controller.all(query_params['page'], query_params['per_page'])

    @jwt_required()
    @user_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creación de Usuarios '''
        controller = UsersController()
        return controller.create(request.json)


@user_ns.route('/<int:id>')
@user_ns.doc(security='Bearer')
class UserById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener un usuario por el ID '''
        controller = UsersController()
        return controller.getById(id)

    @jwt_required()
    @user_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar un usuario por el ID '''
        controller = UsersController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar un usuario por el ID '''
        controller = UsersController()
        return controller.delete(id)


api.add_namespace(user_ns)
