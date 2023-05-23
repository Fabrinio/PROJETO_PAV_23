from flask import Flask
from flask_restful import Api
from .endpoints import initialize_endpoints

from .models.models import db

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:#LFls1412@localhost:5432/PROJETO_PAV2023'

    db.init_app(app)

    #Flask API
    api = Api(app, prefix = "/api")
    initialize_endpoints(api)

    return app