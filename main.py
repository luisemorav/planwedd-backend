from app import app, db, routers

from app.models.base import BaseModel

BaseModel.set_session(db.session)
