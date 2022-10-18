from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship


class BaccountModel(BaseModel):
    __tablename__ = 'cuentas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    banco = Column(String(60))
    nro_cuenta = Column(String(50))
    titular = Column(String(100))
    status = Column(Boolean, default=True)

    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship('UserModel', uselist=False, back_populates='cuentas')