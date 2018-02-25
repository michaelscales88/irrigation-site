from flask import render_template, make_response
from flask_login import login_required
from flask_restful import Resource


class DataAPI(Resource):

    def __init__(self):
        super().__init__()

    def get(self):
        return make_response(
            render_template(
                'data.html',
                title="Data Page"
            )
        )

    @login_required
    def post(self):
        return "Secret Data"
