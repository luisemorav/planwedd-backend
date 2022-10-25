from app import db
from app.models.users_model import UserModel
from app.schemas.users_schema import UsersResponseSchema
# from app.utils.cloudinary import Cloudinary
from flask_jwt_extended import current_user


class UsersController:
    def __init__(self):
        self.model = UserModel
        self.schema = UsersResponseSchema

    def all(self, page, per_page):
        try:
            # Paginate
            # page -> la pagina actual
            # per_page -> total de registros x pagina
            # total -> total de registros
            # pages -> total de paginas
            # items -> Lista de objetos
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

    def getMe(self):
        id = current_user['id']
        try:
            if record := self.model.where(id=id).first():
                response = self.schema(many=False)
                return {
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontro el usuario'
            }, 404
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def create(self, data):
        try:
            if new_record := self.model.where(username=data['username']).first():
                return {
                    'message': 'El usuario solicitado ya existe'
                }, 409

            data['rol_id'] = 2
            new_record = self.model.create(**data)
            new_record.hashPassword()
            db.session.add(new_record)
            db.session.commit()

            response = self.schema(many=False)

            return {
                'message': 'El usuario se creo con exito',
                'data': response.dump(new_record)
            }, 201

        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def update(self, id, data):
        try:
            if record := self.model.where(id=id).first():
                record.update(**data)
                db.session.add(record)
                db.session.commit()

                response = self.schema(many=False)
                return {
                    'messsage': 'El usuario se ha actualizado con exito',
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontro el usuario mencionado'
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
                    'message': 'Se deshabilito el usuario con exito'
                }, 200
            return {
                'message': 'No se encontro el usuario mencionado'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
