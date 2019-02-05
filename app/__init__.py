from flask import Flask
from config import app_config
from app.api.views.user_endpoints import user

def create_app(config_name):
    """Function to create the flask app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config.get(config_name))
    app.register_blueprint(user)
    return app