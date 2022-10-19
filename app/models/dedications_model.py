from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship


class DedicationModel(BaseModel):
    __tablename__ = 'dedicatorias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150))
    contenido = Column(Text, default="")
    status = Column(Boolean, default=True)

    evento_id = Column(Integer, ForeignKey('eventos.id'))
    evento = relationship('EventModel', uselist=False, back_populates='dedicatorias')