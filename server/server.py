from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap, WebCDN
from flask_login import LoginManager, login_required
from flask_restful import reqparse

from .models import BaseModel


db = SQLAlchemy(model_class=BaseModel)
bcrypt = Bcrypt()
login_manager = LoginManager()


def build_server(server):
    with server.app_context():
        # Create database components
        db.init_app(server)
        # Add encryption for Users
        bcrypt.init_app(server)
        # Handle sessions
        login_manager.init_app(server)
        # Add jquery/styling for the website
        Bootstrap(server)
        # Configure external js libraries
        add_cdns(server)

        # Import models that need to be created
        from server.login.models import User
        db.create_all()

        @login_manager.user_loader
        def user_loader(email):
            print("at user_loader", email)
            user = User.find_by_username(email)
            print("at user_loader", user)
            return user if user else None

        @login_manager.request_loader
        def request_loader(request):
            parser = reqparse.RequestParser()
            parser.add_argument('Authorization', location='headers')
            args = parser.parse_args()
            print('arguments', args)
            access_token = User.decode_auth_token(args['Authorization'])
            user = User.get_id(access_token)
            print("at request_loader", user)
            if not user:
                print('returning')
                return

            return user

        # Inject session that models will use
        BaseModel.set_session(db.session)
        return server


def add_cdns(server):
    # server.extensions['bootstrap']['cdns']['migrate'] = WebCDN(
    #     'https://cdnjs.cloudflare.com/ajax/libs/jquery-migrate/1.4.1/'
    # )
    pass
