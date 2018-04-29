# server/default_config.py
import os

# Generate a random session key
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))

BCRYPT_LOG_ROUNDS = 10

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PACKAGE_DIR = os.path.dirname(BASE_DIR)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.environ.get(
    'SQLALCHEMY_DATABASE_URI',
    os.path.join(PACKAGE_DIR, 'instance/local_app.db')
)

LOGIN_DURATION_MINUTES = int(os.environ.get('LOGIN_DURATION_MINUTES', 5))
