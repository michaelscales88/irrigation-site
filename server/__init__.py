# server/__init__.py
from flask import Flask, Blueprint
from flask_restful import Api

from .server import build_server


def create_server(*cfg):
    """
    Creates the server that the html pages interact with.
    """
    server_instance = Flask(
        __name__,
        instance_relative_config=True,
        template_folder='../static/templates',
        static_folder="../static",
    )

    # Settings
    # This program could take multiple different settings files by name.
    server_instance.config.from_object('server.default_config')
    for config_file in cfg:
        server_instance.config.from_pyfile(config_file, silent=True)

    api_bp = Blueprint('backend', __name__)
    api = Api(api_bp)

    # This is where the API are configured so that you can access them
    # with a url.
    from .data import DataAPI
    from .login import LoginAPI, RefreshTokenAPI, AuthenticateTokenAPI
    api.add_resource(LoginAPI, '/', '/login')
    api.add_resource(RefreshTokenAPI, '/refresh-token')
    api.add_resource(AuthenticateTokenAPI, '/authenticate-token')
    api.add_resource(DataAPI, '/data')

    # Register all the API rules with the server
    server_instance.register_blueprint(api_bp)

    return build_server(server_instance)
