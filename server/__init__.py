from flask import Flask, Blueprint
from flask_restful import Api


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

    from .login import LoginAPI
    api.add_resource(LoginAPI, '/', '/login')

    server.register_blueprint(api_bp)

    return server
