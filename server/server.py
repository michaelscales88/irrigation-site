# server/server.py
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_restful import reqparse

from .models import BaseModel


db = SQLAlchemy(model_class=BaseModel)
bcrypt = Bcrypt()
login_manager = LoginManager()
nav = Nav()


def build_server(server):
    """
    Uses the server's context to build all the components of the server.
    This allows the blueprints to access the instance of server that they're
    a part of.
    :param server: Flask App
    :return: Configured Flask App
    """
    with server.app_context():
        # Create database components
        db.init_app(server)
        # Add encryption for Users
        bcrypt.init_app(server)
        # Handle sessions
        login_manager.init_app(server)
        # Add jquery/styling for the website
        Bootstrap(server)
        # Configure navigation
        add_nav_elements()
        nav.init_app(server)

        # Import models that need to be created
        from server.login.models import User
        db.create_all()

        @login_manager.user_loader
        def user_loader(email):
            user = User.find_by_username(email)
            return user if user else None

        @login_manager.request_loader
        def request_loader(request):
            """
            request_loader checks that a valid json web token (jwt)
            exists for the user. If they do not have a valid token
            then they cannot access the resources with @login_required
            :param request:
            :return: A valid user
            """
            parser = reqparse.RequestParser()
            parser.add_argument('Authorization', location='headers')
            args = parser.parse_args()
            access_token = User.decode_auth_token(args['Authorization'])
            user = User.get_id(access_token)
            if not user:
                return

            return user

        # Inject session that models will use
        BaseModel.set_session(db.session)
        return server


def add_nav_elements():
    nav.register_element(
        'top',
        Navbar(
            View('Home', 'backend.loginapi'),
        )
    )
