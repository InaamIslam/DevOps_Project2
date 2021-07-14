from flask import url_for
from flask_testing import TestCase
from application import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_activity(self):
            with patch('random.randrange') as s:
                s.return_value = 0
                response = self.client.get(url_for('activity'))
                self.assertIn(b'Paintballing', response.data)

    def test_activity(self):
            with patch('random.randrange') as s:
                s.return_value = 1
                response = self.client.get(url_for('activity'))
                self.assertIn(b'Paintballing', response.data)
    
    def test_activity(self):
            with patch('random.randrange') as s:
                s.return_value = 2
                response = self.client.get(url_for('activity'))
                self.assertIn(b'Paintballing', response.data)

    def test_activity(self):
            with patch('random.randrange') as s:
                s.return_value = 3
                response = self.client.get(url_for('activity'))
                self.assertIn(b'Paintballing', response.data)