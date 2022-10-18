from flask_seeder import Seeder
from app.models.users_model import UserModel


class UserAdminSeeder(Seeder):
    def run(self):
        users = [
            {
                'nombres': 'Usuario',
                'apellidos': 'Administrador',
                'dni': 'None',
                'username': 'admin',
                'password': '123456',
                'correo': 'administrador@gmail.com',
                'rol_id': 1
            }
        ]

        for user in users:
            exists = UserModel.where(username=user['username']).first()
            if not exists:
                print(f'Se crea administrador: {user}')
                record = UserModel(**user)
                record.hashPassword()
                self.db.session.add(record)
