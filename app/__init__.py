from flask import Flask
from config import app_config
from app.database import create_tables
from app.api.views.user_endpoints import user
from app.api.views.meetup_endpoints import meetup
from app.api.utils.errors import err, bad_request, internal_server_error, not_found, method_not_allowed

def create_app(config_name):
    """Function to create the flask app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config.get(config_name))

    app.register_blueprint(err)
    app.register_blueprint(user)
    app.register_blueprint(meetup)

    app.register_error_handler(404, not_found)
    app.register_error_handler(400, bad_request)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(500, internal_server_error)

    create_tables()
    return app