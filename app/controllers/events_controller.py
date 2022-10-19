from app import db
from app.models.events_model import EventModel
from app.schemas.events_schema import EventsResponseSchema
from app.utils.cloudinary import Cloudinary
from flask_jwt_extended import current_user


class EventsController:
    def __init__(self):
        self.model = EventModel
        self.schema = EventsResponseSchema

    def all(self, page, per_page):
        try:
            records = self.model.where(status=True).order_by('id').paginate(
                per_page=per_page, page=page
            )
            response = self.schema(many=True)
            return {
                'results': response.dump(records.items),
                'pagination': {
                    'totalRecords': records.total,
                    'totalPages': records.pages,
                    'perPage': records.per_page,
                    'currentPage': records.page
                }
            }
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }

    def getById(self, id):
        try:
            if record := self.model.where(id=id).first():
                response = self.schema(many=False)
                return {
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontro el usuario mencionado'
            }, 404
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
        
    def getByUserId(self, id):
        try:
            if record := self.model.where(usuario_id=id, status=True).all():
                response = self.schema(many=True)
                return {
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontraron eventos con en el usuario requerido'
            }, 404
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def create(self, data):
        try:
            cloudinary = Cloudinary()
            image_url = cloudinary.uploadImage(data['img_portada'])

            data['img_portada'] = image_url
            data['usuario_id'] = current_user['id']
            new_record = self.model.create(**data)
            db.session.add(new_record)
            db.session.commit()

            response = self.schema(many=False)

            return {
                'message': 'El evento se creo con exito',
                'data': response.dump(new_record)
            }


        except Exception as err:
            db.session.rollback()
            return {
                'message': str(err)
            }, 500

        

    def update(self, id, data):
        try:
            if record := self.model.where(id=id).first():
                record.update(**data)
                db.session.add(record)
                db.session.commit()

                response = self.schema(many=False)
                return {
                    'messsage': 'El evento se ha actualizado con exito',
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontro el evento mencionado'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def delete(self, id):
        try:
            if record := self.model.where(id=id).first():
                if record.status:
                    record.update(status=False)
                    db.session.add(record)
                    db.session.commit()
                return {
                    'message': 'Se deshabilito el evento con exito'
                }, 200
            return {
                'message': 'No se encontro el evento mencionado'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
