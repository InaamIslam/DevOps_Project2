from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import requests_mock
from app import app

class TestBase(TestCase):
    def create_app(self):
        app.config.update(DEBUG=True)
        return app

# class TestResponse(TestBase):
#     def test_service1(self):
#         with patch("requests.get") as a:
#                 with patch("requests.get") as b:
#                     with patch("requests.post") as c:
#                         a.return_value.text = "London"
#                         b.return_value.text = "Paintballing"
#                         c.return_value.text = "200"

#                 response = self.client.get(url_for('index'))
#                 self.assertIn(b'The total cost of your holiday will be 200 GBP', response.data)

class TestService1(TestBase):
    def test_service1(self):
        with requests_mock.Mocker() as mocker:
            mocker.get("http://service_2_api:5000/city", text='London')
            mocker.get("http://service_3_api:5000/activity", text='Paintballing')
            mocker.post("http://service_4_api:5000/price", text='200') 
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The total cost of your holiday will 200 GBP', response.data)