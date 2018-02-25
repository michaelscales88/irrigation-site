# server/default_config.py
import os

SECRET_KEY = os.urandom(24)  # Generate a random session key
BCRYPT_LOG_ROUNDS = 10

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PACKAGE_DIR = os.path.dirname(BASE_DIR)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    os.path.join(PACKAGE_DIR, 'instance/local_app.db')
)

