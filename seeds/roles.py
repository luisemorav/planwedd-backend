from flask_seeder import Seeder
from app.models.roles_model import RoleModel


class RoleSeeder(Seeder):
    def run(self):
        roles = [
            {
                'name': 'Administrador'
            },
            {
                'name': 'Usuario'
            }
        ]

        for role in roles:
            exists = RoleModel.where(name=role['name']).first()
            if not exists:
                print(f'Se crea rol: {role}')
                record = RoleModel(**role)
                self.db.session.add(record)
