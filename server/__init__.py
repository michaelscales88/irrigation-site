from flask import Flask, Blueprint
from flask_restful import Api

from .server import build_server


def create_server(*cfg):
    server = Flask(
        __name__,
        instance_relative_config=True,
        template_folder='../static/templates',
        static_folder="../static",
    )

    # Settings
    server.config.from_object('server.default_config')
    for config_file in cfg:
        server.config.from_pyfile(config_file, silent=True)

    api_bp = Blueprint('backend', __name__)
    api = Api(api_bp)

    from .data import DataAPI
    from .login import LoginAPI, RefreshTokenAPI, AuthenticateTokenAPI
    api.add_resource(LoginAPI, '/', '/login')
    api.add_resource(RefreshTokenAPI, '/refresh-token')
    api.add_resource(AuthenticateTokenAPI, '/authenticate-token')
    api.add_resource(DataAPI, '/data')

    server.register_blueprint(api_bp)

    return build_server(server)
