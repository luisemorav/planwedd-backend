from app import db
from app.models.dedications_model import DedicationModel
from app.schemas.dedications_schema import DedicationsResponseSchema

class DedicationsController:
    def __init__(self):
        self.model = DedicationModel
        self.schema = DedicationsResponseSchema

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
                'message': 'No se encontro la dedicatoria requerida'
            }, 404
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def getByEventId(self, id):
        try:
            if record := self.model.where(evento_id=id).all():
                response = self.schema(many=True)
                return {
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontraron dedicatorias con en el evento requerido'
            }, 404
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def create(self, data):
        try:
            new_record = self.model.create(**data)
            db.session.add(new_record)
            db.session.commit()

            response = self.schema(many=False)

            return {
                'message': 'La dedicatoria se creo con exito',
                'data': response.dump(new_record)
            }
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }

    def update(self, id, data):
        try:
            if record := self.model.where(id=id).first():
                record.update(**data)
                db.session.add(record)
                db.session.commit()

                response = self.schema(many=False)
                return {
                    'messsage': 'La dedicatoria se ha actualizado con exito',
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontro la dedicatoria requerida'
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
                    'message': 'Se elimino la dedicatoria con exito'
                }, 200
            return {
                'message': 'No se encontro la dedicatoria requerida'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
