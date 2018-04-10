# data/api.py
from flask import render_template, make_response
from flask_login import login_required
from flask_restful import Resource


class DataAPI(Resource):

    def __init__(self):
        """
        This constructor gets called whenever this api is called.
        """
        super().__init__()

    def get(self):
        """
        Gets the data page that has the iFrame.
        :return:
        """
        return make_response(
            render_template(
                'data.html',
                title="Data Page"
            )
        )

    @login_required
    def post(self):
        return "Secret Data"
