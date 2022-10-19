from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship


class GiftModel(BaseModel):
    __tablename__ = 'regalos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(200))
    descripcion = Column(Text, default="")
    img_regalo = Column(String, nullable=True)
    precio = Column(String(10))
    status = Column(Boolean, default=True)

    evento_id = Column(Integer, ForeignKey('eventos.id'))
    evento = relationship('EventModel', uselist=False, back_populates='regalos')
