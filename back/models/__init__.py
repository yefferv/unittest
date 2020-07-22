from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app(enviroment):
    
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(enviroment)
    db.init_app(app)

    with app.app_context():
        from back.routes import customer, socket, measurer
        db.create_all()  
        return app