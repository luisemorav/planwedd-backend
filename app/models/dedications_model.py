from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class DedicationModel(BaseModel):
    __tablename__ = 'dedicatorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(120))
    contenido = Column(String(400), default="")
    status = Column(Boolean, default=True)

    evento_id = Column(Integer, ForeignKey('eventos.id'))
    evento = relationship('EventModel', uselist=False, back_populates='dedicatorias')