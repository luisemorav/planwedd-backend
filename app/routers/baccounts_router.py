from app import api
from flask import request
from flask_restx import Resource
from app.schemas.baccounts_schema import BaccountsRequestSchema
from app.controllers.baccounts_controller import BaccountsController
from flask_jwt_extended import jwt_required

baccount_ns = api.namespace(
    name='Cuentas',
    description='Rutas del modulo de Cuentas Bancarias',
    path='/baccounts'
)

request_schema = BaccountsRequestSchema(baccount_ns)

@baccount_ns.route('')
@baccount_ns.doc(security='Bearer')
class Baccounts(Resource):
    @jwt_required()
    @baccount_ns.expect(request_schema.all())
    def get(self):
        ''' Listar todas las cuentas '''
        query_params = request_schema.all().parse_args()
        controller = BaccountsController()
        return controller.all(query_params['page'], query_params['per_page'])

    @jwt_required()
    @baccount_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creación de Cuenta '''
        controller = BaccountsController()
        return controller.create(request.json)


@baccount_ns.route('/<int:id>')
@baccount_ns.doc(security='Bearer')
class BaccountById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener una cuenta por el ID '''
        controller = BaccountsController()
        return controller.getById(id)

    @jwt_required()
    @baccount_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar una cuenta por el ID '''
        controller = BaccountsController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar una cuenta por el ID '''
        controller = BaccountsController()
        return controller.delete(id)

api.add_namespace(baccount_ns)