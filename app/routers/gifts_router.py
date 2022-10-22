from app import api
from flask import request
from flask_restx import Resource
from app.schemas.gifts_schema import GiftsRequestSchema
from app.controllers.gifts_controller import GiftsController
from flask_jwt_extended import jwt_required

gift_ns = api.namespace(
    name='Regalos',
    description='Rutas del modulo de Regalos',
    path='/gifts'
)

request_schema = GiftsRequestSchema(gift_ns)

@gift_ns.route('')
@gift_ns.doc(security='Bearer')
class Gifts(Resource):
    @jwt_required()
    @gift_ns.expect(request_schema.all())
    def get(self):
        ''' Listar todos los regalos '''
        query_params = request_schema.all().parse_args()
        controller = GiftsController()
        return controller.all(query_params['page'], query_params['per_page'])

    @jwt_required()
    @gift_ns.expect(request_schema.create(), validate=True)
    def post(self):
        ''' Creación de Regalos '''
        form = request_schema.create().parse_args()
        controller = GiftsController()
        return controller.create(form)

@gift_ns.route('/soft')
@gift_ns.doc(security='Bearer')
class GiftsSoft(Resource):
    @jwt_required()
    @gift_ns.expect(request_schema.createsoft(), validate=True)
    def post(self):
        ''' Creación de Regalos predeterminados '''
        form = request_schema.createsoft().parse_args()
        controller = GiftsController()
        return controller.createsoft(form)


@gift_ns.route('/<int:id>')
@gift_ns.doc(security='Bearer')
class GiftById(Resource):

    

    @jwt_required()
    def get(self, id):
        ''' Obtener un regalo por el ID '''
        controller = GiftsController()
        return controller.getById(id)


    @jwt_required()
    @gift_ns.expect(request_schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar un regalo por el ID '''
        controller = GiftsController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar un regalo por el ID '''
        controller = GiftsController()
        return controller.delete(id)

@gift_ns.route('/event<int:id>')
class GiftsByEventId(Resource):
    def get(self, id):
        ''' Obtener regalos por el ID del evento'''
        controller = GiftsController()
        return controller.getByEventId(id)

api.add_namespace(gift_ns)
