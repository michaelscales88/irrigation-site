# project/tests/test_user_model.py

import unittest

from server.server import db
from server.login.models import User
from server.tests.test_config import TestDevelopmentConfig


class TestUserModel(TestDevelopmentConfig):

    def test_encode_auth_token(self):
        user = User(
            email='test@test.com',
            password='test'
        )
        db.session.add(user)
        db.session.commit()
        auth_token = user.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token) == 1)


if __name__ == '__main__':
    unittest.main()
