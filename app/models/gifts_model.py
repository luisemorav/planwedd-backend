from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship


class GiftModel(BaseModel):
    __tablename__ = 'regalos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    descripcion = Column(String(300), default="")
    img_regalo = Column(Text, nullable=True)
    precio = Column(String(12), default="0")
    status = Column(Boolean, default=True)

    evento_id = Column(Integer, ForeignKey('eventos.id'))
    evento = relationship('EventModel', uselist=False, back_populates='regalos')
