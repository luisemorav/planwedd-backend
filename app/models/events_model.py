from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship


class EventModel(BaseModel):
    __tablename__ = 'eventos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_evento = Column(String(200))
    fecha_evento = Column(Date, default="")
    texto_portada = Column(String(300), default="")
    img_portada = Column(String(50))
    configuraciones = Column(String(200))
    status = Column(Boolean, default=True)

    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    usuario = relationship('UserModel', uselist=False, back_populates='eventos')

    regalos = relationship('GiftModel', uselist=True, back_populates='evento')

    dedicatorias = relationship('DedicationModel', uselist=True, back_populates='evento')