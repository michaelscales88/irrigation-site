from flask import render_template, make_response, jsonify
from flask_restful import Resource, reqparse
from flask_login import login_required

from .models import User


class LoginAPI(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_name')
        parser.add_argument('user_password')
        self.args = parser.parse_args()
        super().__init__()

    def __del__(self):
        User.session.commit()

    def get(self):
        return make_response(
            render_template(
                'login.html',
                title="Login Page"
            )
        )

    def post(self):
        user = User.find_by_username(self.args['user_name'])
        if user and user.check_password(self.args['user_password']):
            token = user.encode_auth_token(user.id).decode()
            return jsonify(
                auth_token=token,
                authenticated=True
            )

    @login_required
    def put(self):
        user = User('test@email.com', '1234')
        user.save()
        print(user)


class AuthenticateTokenAPI(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Authorization', location='headers')
        self.args = parser.parse_args()
        super().__init__()

    def post(self):
        access_token = User.decode_auth_token(self.args['Authorization'])
        print(access_token)
        user = User.get_id(access_token)
        print(user)
        if user:
            token = user.encode_auth_token(user.id).decode()
            print("refresh-token", token)
            return jsonify(
                auth_token=token,
                authenticated=True
            )


class RefreshTokenAPI(Resource):

    def __init__(self):
        parser = reqparse.RequestParser()
        parser.add_argument('Authorization', location='headers')
        self.args = parser.parse_args()
        super().__init__()

    def post(self):
        access_token = User.decode_auth_token(self.args['Authorization'])
        print(access_token)
        user = User.get_id(access_token)
        print(user)
        if user:
            token = user.encode_auth_token(user.id).decode()
            print("refresh-token", token)
            return jsonify(
                auth_token=token,
                authenticated=True
            )
