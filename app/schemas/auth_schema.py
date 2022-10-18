from flask_restx import fields
from flask_restx.reqparse import RequestParser


class AuthRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def signIn(self):
        return self.namespace.model('Auth SignIn', {
            'username': fields.String(required=True),
            'password': fields.String(required=True)
        })

    def resetPassword(self):
        return self.namespace.model('Auth Reset Password', {
            'correo': fields.String(required=True)
        })

    def refreshToken(self):
        parser = RequestParser()
        parser.add_argument(
            'Authorization',
            type=str, location='headers',
            help='Ex: Bearer {refresh_token}'
        )
        return parser
