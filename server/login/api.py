# login/api.py
from flask import render_template, make_response, jsonify
from flask_restful import Resource, reqparse
from flask_login import login_required

from .models import User


class LoginAPI(Resource):

    def __init__(self):
        """
        This constructor gets called whenever this api is called.
        It parses the json and converts the variables into the
        variables the the api needs.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('user_name')
        parser.add_argument('user_password')
        self.args = parser.parse_args()
        super().__init__()

    def __del__(self):
        # Commit to the database at the end of the request
        User.session.commit()

    def get(self):
        """
        Gets a default user because id is hardcoded 1. If there is not
        user associated with id 1 an admin is created with the password 1234.
        :return: the login page
        """
        user = User.get_id(1)
        if not user:
            user = User("admin@email.com", '1234', admin=True)
            user.save()
        return make_response(
            render_template(
                'login.html',
                title="Login Page"
            )
        )

    def post(self):
        """
        Logs a user in. Checks for the user based on the given user_name.
        If the user is found, then it checks the password. If the password
        is valid then the user gets a json web token (jwt).
        :return:
        """
        user = User.find_by_username(self.args['user_name'])
        if user and user.check_password(self.args['user_password']):
            token = user.encode_auth_token(user.id).decode()
            return jsonify(
                auth_token=token,
                authenticated=True
            )

    @login_required
    def put(self):
        """
        Test adding a user with the password 1234
        :return:
        """
        user = User('test@email.com', '1234')
        user.save()
        print(user)


class AuthenticateTokenAPI(Resource):

    def __init__(self):
        """
        This constructor gets called whenever this api is called.
        It parses the json and converts the variable from the headers
        to check for authorization to view the page.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('Authorization', location='headers')
        self.args = parser.parse_args()
        super().__init__()

    def post(self):
        """
        Decode the json web token (jwt). If the token is valid it will return a
        user. If the user is valid then they are authenticated and need a new
        jwt.
        :return True authenticated status and a new jwt.
        """
        access_token = User.decode_auth_token(self.args['Authorization'])
        user = User.get_id(access_token)
        if user:
            token = user.encode_auth_token(user.id).decode()
            return jsonify(
                auth_token=token,
                authenticated=True
            )


class RefreshTokenAPI(Resource):

    def __init__(self):
        """
        This constructor gets called whenever this api is called.
        It parses the json and converts the variable from the headers
        to check for authorization to view the page.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('Authorization', location='headers')
        self.args = parser.parse_args()
        super().__init__()

    def post(self):
        """
        Decode the json web token (jwt). If the token is valid it will return a
        user. If the user is valid then they are authenticated and need a new
        jwt.
        :return True authenticated status and a new jwt.
        """
        access_token = User.decode_auth_token(self.args['Authorization'])
        user = User.get_id(access_token)
        if user:
            token = user.encode_auth_token(user.id).decode()
            return jsonify(
                auth_token=token,
                authenticated=True
            )
