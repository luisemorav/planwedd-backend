from app import api
from flask import request
from flask_restx import Resource
from app.schemas.dedications_schema import DedicationsRequestSchema
from app.controllers.dedications_controller import DedicationsController
from flask_jwt_extended import jwt_required

dedication_ns = api.namespace(
    name='Dedicatorias',
    description='Rutas del modulo de Dedicatorias',
    path='/dedications'
)

request_schema = DedicationsRequestSchema(dedication_ns)

@dedication_ns.route('')
@dedication_ns.doc(security='Bearer')
class Dedications(Resource):
    @jwt_required()
    @dedication_ns.expect(request_schema.all())
    def get(self):
        ''' Listar todas las dedicatorias '''
        query_params = request_schema.all().parse_args()
        controller = DedicationsController()
        return controller.all(query_params['page'], query_params['per_page'])

    @jwt_required()
    @dedication_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creación de Dedicatorias '''
        controller = DedicationsController()
        return controller.create(request.json)


@dedication_ns.route('/<int:id>')
@dedication_ns.doc(security='Bearer')
class DedicationById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener una dedicatoria por el ID '''
        controller = DedicationsController()
        return controller.getById(id)

    @jwt_required()
    @dedication_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar una dedicatoria por el ID '''
        controller = DedicationsController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar una dedicatoria por el ID '''
        controller = DedicationsController()
        return controller.delete(id)

@dedication_ns.route('/event<int:id>')
class DedicationsByEventId(Resource):
    def get(self, id):
        ''' Obtener dedicatorias por el ID del evento'''
        controller = DedicationsController()
        return controller.getByEventId(id)

api.add_namespace(dedication_ns)