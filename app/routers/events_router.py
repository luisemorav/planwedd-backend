from app import api
from flask import request
from flask_restx import Resource
from app.schemas.events_schema import EventsRequestSchema
from app.controllers.events_controller import EventsController
from flask_jwt_extended import jwt_required

event_ns = api.namespace(
    name='Eventos',
    description='Rutas del modulo Eventos',
    path='/events'
)

request_schema = EventsRequestSchema(event_ns)

@event_ns.route('')
@event_ns.doc(security='Bearer')
class Events(Resource):
    @jwt_required()
    @event_ns.expect(request_schema.all())
    def get(self):
        ''' Listar todos los eventos '''
        query_params = request_schema.all().parse_args()
        controller = EventsController()
        return controller.all(query_params['page'], query_params['per_page'])

    @jwt_required()
    @event_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creación de Eventos '''
        controller = EventsController()
        return controller.create(request.json)


@event_ns.route('/<int:id>')
@event_ns.doc(security='Bearer')
class EventById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener un evento por el ID '''
        controller = EventsController()
        return controller.getById(id)

    @jwt_required()
    @event_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar un evento por el ID '''
        controller = EventsController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar un evento por el ID '''
        controller = EventsController()
        return controller.delete(id)

api.add_namespace(event_ns)