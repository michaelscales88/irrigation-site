import jwt
from datetime import datetime, timedelta
from flask import current_app
from flask_login import UserMixin

from ..server import bcrypt, db


class User(db.Model, UserMixin):
    """ User Model for storing user related details """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(str(password))
        self.registered_on = datetime.now()
        self.admin = admin

    @classmethod
    def get_id(cls, id):
        return cls.query.filter(cls.id == id).first()

    @classmethod
    def find_by_username(cls, user_name):
        return cls.query.filter(cls.email == user_name).first()

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=0, seconds=30),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY', 'I AM A SECRET'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
