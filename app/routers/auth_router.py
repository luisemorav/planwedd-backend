from app import api, mail
from flask import request
from flask_restx import Resource
from app.schemas.auth_schema import AuthRequestSchema
from app.schemas.users_schema import UsersRequestSchema
from app.controllers.auth_controller import AuthController
from app.controllers.users_controller import UsersController
from flask_jwt_extended import jwt_required, get_jwt_identity


auth_ns = api.namespace(
    name='Autenticación',
    description='Rutas del modulo Autenticación',
    path='/auth'
)


request_schema = AuthRequestSchema(auth_ns)
user_schema = UsersRequestSchema(auth_ns)


@auth_ns.route('/signin')
class SignIn(Resource):
    @auth_ns.expect(request_schema.signIn(), validate=True)
    def post(self):
        ''' Crear token de autenticación '''
        controller = AuthController()
        return controller.signIn(request.json)


@auth_ns.route('/signup')
class SignUp(Resource):
    @auth_ns.expect(user_schema.create(), validate=True)
    def post(self):
        ''' Creación de Usuarios '''
        controller = UsersController()
        return controller.create(request.json)


@auth_ns.route('/reset_password')
class ResetPassword(Resource):
    @auth_ns.expect(request_schema.resetPassword(), validate=True)
    def post(self):
        ''' Resetear la contraseña de un usuario '''
        controller = AuthController()
        return controller.resetPassword(request.json)


@auth_ns.route('/token/refresh')
class TokenRefresh(Resource):
    @auth_ns.expect(request_schema.refreshToken())
    @jwt_required(refresh=True)
    def post(self):
        ''' Obtener un nuevo access_token desde el refresh_token '''
        identity = get_jwt_identity()
        controller = AuthController()
        return controller.refreshToken(identity)


api.add_namespace(auth_ns)
