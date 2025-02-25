from flask import Flask, Blueprint
from app.routes.main.routes import main
from app.config import SECRET_KEY

def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY
 
    app.register_blueprint(main)

    return app
