from flask import current_app
from unittest import TestCase


class TestDevelopmentConfig(TestCase):

    def create_current_app(self):
        current_app.config.from_object('server.default_config')
        return current_app

    def test_current_app_is_development(self):
        self.assertFalse(current_app.config['SECRET_KEY'] is 'my_precious')
        self.assertTrue(current_app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            current_app.config['SQLALCHEMY_DATABASE_URI'] == "sqlite:///instance/local_app.db"
        )


class TestTestingConfig(TestCase):

    def create_current_app(self):
        current_app.config.from_object('server.default_config')
        return current_app

    def test_current_app_is_testing(self):
        self.assertTrue(current_app.config['DEBUG'])
        self.assertTrue(
            current_app.config['SQLALCHEMY_DATABASE_URI'] == "sqlite:///instance/local_app.db"
        )

