from flask_restful import Resource
from flask import render_template, make_response


class LoginAPI(Resource):

    def __init__(self):

        super().__init__()

    def get(self):
        return make_response(
            render_template('login.html')
        )
