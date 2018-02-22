from flask import Flask


def create_server(*cfg):
    server = Flask(
        __name__,
        instance_relative_config=True
    )

    # Settings
    server.config.from_object('server.default_config')
    for config_file in cfg:
        server.config.from_pyfile(config_file, silent=True)

    return server
