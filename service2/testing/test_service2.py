from flask import url_for
from flask_testing import TestCase
from application import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_city(self):
            with patch('random.randrange') as s:
                s.return_value = 0
                response = self.client.get(url_for('city'))
                self.assertIn(b'London', response.data)

    def test_city(self):
            with patch('random.randrange') as s:
                s.return_value = 1
                response = self.client.get(url_for('city'))
                self.assertIn(b'Barcelona', response.data)

    def test_city(self):
            with patch('random.randrange') as s:
                s.return_value = 2
                response = self.client.get(url_for('city'))
                self.assertIn(b'Milan', response.data)

    def test_city(self):
            with patch('random.randrange') as s:
                s.return_value = 3
                response = self.client.get(url_for('city'))
                self.assertIn(b'Tokyo', response.data)
   