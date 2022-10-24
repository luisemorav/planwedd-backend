from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from bcrypt import hashpw, gensalt, checkpw


class UserModel(BaseModel):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(120))
    apellidos = Column(String(160))
    dni = Column(String(8), unique=True)
    username = Column(String(80), unique=True)
    password = Column(String(120), nullable=False)
    # img = Column(String(255), nullable=True)
    correo = Column(String(120), unique=True)
    status = Column(Boolean, default=True)


    rol_id = Column(Integer, ForeignKey('roles.id'), default=1)
    rol = relationship('RoleModel', uselist=False, back_populates='usuarios')

    eventos = relationship('EventModel', uselist=True, back_populates='usuario')

    cuentas = relationship('BaccountModel', uselist=True, back_populates='usuario')

    def hashPassword(self):
        pwd_encode = self.password.encode('utf-8')
        pwd_hash = hashpw(pwd_encode, gensalt(rounds=10))
        self.password = pwd_hash.decode('utf-8')

    def checkPassword(self, password):
        return checkpw(
            password.encode('utf-8'),
            self.password.encode('utf-8')
        )
