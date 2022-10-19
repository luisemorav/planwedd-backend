from os import getenv
from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_cors import CORS
from flask_seeder import FlaskSeeder
from config import config_env

app = Flask(__name__)
CORS(app)
app.config.from_object(config_env[getenv('FLASK_ENV')])

authorizations = {
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    app,
    title='Planwedd',
    version='1.0',
    description='Endpoints de Planwedd.',
    authorizations=authorizations,
    doc='/swagger-ui'
)

db = SQLAlchemy(app)
migrate = Migrate(app=app, db=db, compare_type=True)

jwt = JWTManager(app)
mail = Mail(app)

seeder = FlaskSeeder(app, db)
