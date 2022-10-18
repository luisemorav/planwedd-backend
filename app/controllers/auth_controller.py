from app import db
from app.models.users_model import UserModel
from flask_jwt_extended import create_access_token, create_refresh_token
from secrets import token_hex
from app.utils.mailing import Mailing


class AuthController:
    def __init__(self):
        self.model = UserModel
        self.schema = ''
        self.mailing = Mailing()

    def signIn(self, data):
        try:
            if record := self.model.where(
                username=data.get('username'),
                status=True
            ).first():
                if record.checkPassword(data.get('password')):
                    access_token = create_access_token(
                        identity=record.id
                    )
                    refresh_token = create_refresh_token(
                        identity=record.id
                    )
                    return {
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }, 200
                else:
                    raise Exception('La contraseña ingresada es incorrecta')

            raise Exception('No se encontro el usuario')
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def resetPassword(self, data):
        try:
            if record := self.model.where(
                correo=data.get('correo'),
                status=True
            ).first():
                new_password = token_hex(5)
                record.password = new_password
                record.hashPassword()
                
                self.mailing.emailResetPassword(record.correo, new_password)

                db.session.add(record)
                db.session.commit()
                return {
                    'message': 'Se envio un correo con tu nueva contraseña'
                }, 200
            raise Exception('No se encontro el usuario')
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def refreshToken(self, identity):
        try:
            access_token = create_access_token(
                identity=identity
            )
            return {
                'access_token': access_token
            }, 200
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
