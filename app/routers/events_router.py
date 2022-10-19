from app import api
from flask import request, jsonify
from flask_restx import Resource
from app.schemas.events_schema import EventsRequestSchema
from app.controllers.events_controller import EventsController
from flask_jwt_extended import jwt_required
from app.utils.cloudinary import Cloudinary

event_ns = api.namespace(
    name='Eventos',
    description='Rutas del modulo Eventos',
    path='/events'
)

request_schema = EventsRequestSchema(event_ns)

@event_ns.route('')
@event_ns.doc(security='Bearer')
class Events(Resource):
    # jwt_required()
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
        form = request_schema.create().parse_args()
        controller = EventsController()
        return controller.create(form)

# @event_ns.route('/uploadimage')
# @event_ns.doc(security='Bearer')
# class UploadImage(Resource):
#     # @jwt_required()
#     def post(self):
#         try:
#             cloudinary = Cloudinary()
#             response = cloudinary.upload(request.files['imagen'])
#             return jsonify({
#                 'url': response
#             }), 200
#         except Exception as err:
#             return {
#                 'message': str(err)
#             }, 500


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

@event_ns.route('<int:id>')
class EventByUserId(Resource):
    def get(self, id):
        ''' Obtener un evento por el UserID '''
        controller = EventsController()
        return controller.getByUserId(id)

api.add_namespace(event_ns)