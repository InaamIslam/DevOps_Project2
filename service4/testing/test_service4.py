from flask import url_for
from flask_testing import TestCase
from application import app
from unittest.mock import patch
import requests_mock


class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_London_Paintball(self):
        with patch('requests.get') as a:
            a.return_value.text = 'London'
            with patch('random.randrange') as b:
                    b.return_value = 'Paintballing'
                    response = self.client.post(
                        url_for('price'),
                        data = 'London Paintballing')
                    self.assertEqual(b'200', response.data)

    def test_London_surfing(self):
        with patch('requests.get') as a:
            a.return_value.text = 'London'
            with patch('random.randrange') as b:
                    b.return_value = 'Surfing'
                    response = self.client.post(
                        url_for('price'),
                        data = 'London Surfing')
                    self.assertIn(b'400', response.data)

    def test_London_snorkelling(self):
        with patch('requests.get') as a:
            a.return_value.text = 'London'
            with patch('random.randrange') as b:
                    b.return_value = 'Snorkelling'
                    response = self.client.post(
                        url_for('price'),
                        data = 'London Snorkelling')
                    self.assertIn(b'600', response.data)

    def test_London_skiing(self):
        with patch('requests.get') as a:
            a.return_value.text = 'London'
            with patch('random.randrange') as b:
                    b.return_value = 'Skiing'
                    response = self.client.post(
                        url_for('price'),
                        data = 'London Skiing')
                    self.assertIn(b'800', response.data)

    def test_Barcelona_Paintball(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Barcelona'
            with patch('random.randrange') as b:
                    b.return_value = 'Paintballing'
                    response = self.client.post(
                        url_for('price'),
                        data = 'Barcelona Paintballing')
                    self.assertIn(b'200', response.data)


    def test_Barcelona_surfing(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Barcelona'
            with patch('random.randrange') as b:
                    b.return_value = 'Surfing'
                    response = self.client.post(
                        url_for('price'),
                        data = 'Barcelona Surfing')
                    self.assertIn(b'400', response.data)

    def test_Barcelona_snorkelling(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Barcelona'
            with patch('random.randrange') as b:
                    b.return_value = 'Snorkelling'
                    response = self.client.post(
                        url_for('price'),
                        data = 'Barcelona Snorkelling')
                    self.assertIn(b'600', response.data)

    def test_Barcelona_skiing(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Barcelona'
            with patch('random.randrange') as b:
                    b.return_value = 'Skiing'
                    response = self.client.post(
                        url_for('price'),
                        data = 'Barcelona Skiing')
                    self.assertIn(b'800', response.data)
    
    def test_Milan_Paintball(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Milan'
            with patch('random.randrange') as b:
                    b.return_value = 'Paintballing'
                    response = self.client.post(
                        url_for('price'),
                        data = 'Milan Paintballing')
                    self.assertIn(b'200', response.data)

                    

    def test_Milan_surfing(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Milan'
            with patch('random.randrange') as b:
                    b.return_value = 'Surfing'
                    response = self.client.post(
                        url_for('price'),
                        data = 'Milan Surfing')
                    self.assertIn(b'400', response.data)

    def test_Milan_snorkelling(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Milan'
            with patch('random.randrange') as b:
                    b.return_value = 'Snorkelling'
                    response = self.client.post(
                        url_for('price'),
                        data = 'Milan Snorkelling')
                    self.assertIn(b'600', response.data)

    def test_Milan_skiing(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Milan'
            with patch('random.randrange') as b:
                    b.return_value = 'Skiing'
                    response = self.client.post(
                        url_for('price'),
                        data = 'Milan Skiing')
                    self.assertIn(b'800', response.data)


    def test_Tokyo_Paintball(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Tokyo'
            with patch('random.randrange') as b:
                    b.return_value = 'Paintablling'
                    response = self.client.post(
                        url_for('price'),
                        data = 'Tokyo Paintballing')
                    self.assertIn(b'200', response.data)

                    

    def test_Tokyo_surfing(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Tokyo'
            with patch('random.randrange') as b:
                    b.return_value = 'Surfing'
                    response = self.client.post(
                        url_for('price'),
                        data = 'Tokyo Surfing')
                    self.assertIn(b'400', response.data)

    def test_Tokyo_snorkelling(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Tokyo'
            with patch('random.randrange') as b:
                    b.return_value = 'Snorkelling'
                    response = self.client.post(
                        url_for('price'),
                        data = 'Tokyo Snorkelling')
                    self.assertIn(b'600', response.data)

    def test_Tokyo_skiing(self):
        with patch('requests.get') as a:
            a.return_value.text = 'Tokyo'
            with patch('random.randrange') as b:
                    b.return_value = 'Skiing'
                    response = self.client.post(
                        url_for('price'),
                        data = 'Tokyo Skiing')
                    self.assertIn(b'800', response.data)


    
   

  