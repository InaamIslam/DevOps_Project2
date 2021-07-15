from flask import url_for
from flask_testing import TestCase
from application import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        app.config.update(DEBUG=True)
        return app

class TestService2(TestBase):
    def test_all_cities(self):
        for _ in range(20):
            response = self.client.get(url_for('city'))
            self.assertIn(response.data.decode("utf-8"),["London", "Barcelona", "Milan", "Tokyo"])

class TestService2(TestBase):
    def test_London(self):
        with patch('random.choice') as s:
            s.return_value = 'London'
            response = self.client.get(url_for('city'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(b'London', response.data)

    def test_Barcelona(self):
        with patch('random.choice') as s:
            s.return_value = 'Barcelona'
            response = self.client.get(url_for('city'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Barcelona', response.data)

    def test_Milan(self):
        with patch('random.choice') as s:
            s.return_value = 'Milan'
            response = self.client.get(url_for('city'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Milan', response.data)
    
    def test_Tokyo(self):
        with patch('random.choice') as s:
            s.return_value = 'Tokyo'
            response = self.client.get(url_for('city'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Tokyo', response.data)


   
