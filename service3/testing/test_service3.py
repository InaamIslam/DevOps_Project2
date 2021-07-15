from flask import url_for
from flask_testing import TestCase
from application import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestService3(TestBase):
    def test_all_activities(self):
        for _ in range(20):
            response = self.client.get(url_for('activity'))
            self.assertIn(response.data.decode("utf-8"),["Paintballing", "Surfing", "Snorkelling", "Skiing"])

class TestService2(TestBase):
    def test_paintballing(self):
        with patch('random.choice') as s:
            s.return_value = 'Paintballing'
            response = self.client.get(url_for('activity'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(b'Paintballing', response.data)

    def test_surfing(self):
        with patch('random.choice') as s:
            s.return_value = 'Surfing"'
            response = self.client.get(url_for('activity'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(b'Surfing"', response.data)
    
    def test_snorkelling(self):
        with patch('random.choice') as s:
            s.return_value = 'Snorkelling'
            response = self.client.get(url_for('activity'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(b'Snorkelling', response.data)

    def test_skiing(self):
        with patch('random.choice') as s:
            s.return_value = 'Skiing'
            response = self.client.get(url_for('activity'))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(b'Skiing', response.data)

