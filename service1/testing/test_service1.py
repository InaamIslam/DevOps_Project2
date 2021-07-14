from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch
import requests_mock
import requests

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app


# class TestResponse(TestBase):
#     def test_service1(self):
#         with patch("requests.get") as a:
#             with patch("requests.get") as c: 
#                 with patch("requests.post") as b:
#                     a.return_city.text = "London"
#                     c.return_activity = "Paintballing"
#                     b.return_price.text = "£200 - £400"
#                 response = self.client.get(url_for('/'))
#                 self.assertIn(b'The total cost of your holiday will be between £200 - £400', response.data)


class TestService1(TestBase):
    def test_service1(self):
        with requests_mock.Mocker() as mocker:
            mocker.get("http://service_2_api:5000/city", text='London')
            mocker.post("http://service_4_api:5000/price", text='£200 - £400') 
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn("The total cost of your holiday will be between £200 - £400", response.data)