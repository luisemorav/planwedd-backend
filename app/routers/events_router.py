from app import api
from flask import request, jsonify
from flask_restx import Resource
from app.schemas.events_schema import EventsRequestSchema
from app.controllers.events_controller import EventsController
from flask_jwt_extended import jwt_required
import cloudinary
import cloudinary.uploader

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
        controller = EventsController()
        return controller.create(request.json)

@event_ns.route('/uploadimage')
@event_ns.doc(security='Bearer')
class UploadImage(Resource):
    # @jwt_required()
    def post(self):
        try:
            cloudinary.config( 
                cloud_name = "de3i8hs61", 
                api_key = "697852552381113", 
                api_secret = "SGthDnSL6NpdHh6TloTBl-crRPk" 
            )
            ret = cloudinary.uploader.upload(request.files['imagen'])
            response = jsonify(list(ret))
            return response, 201
        except Exception as err:
            return {
                'message': str(err)
            }, 500


@event_ns.route('/<int:id>')
@event_ns.doc(security='Bearer')
class EventById(Resource):
    # @jwt_required()
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