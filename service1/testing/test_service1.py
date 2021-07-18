from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app

class TestBase(TestCase):
    def create_app(self):
        # app.config.update(DEBUG=True)
        return app

class TestService1(TestBase):
    def test_service1(self):
        with requests_mock.Mocker() as mocker:
            mocker.get("http://service_2_api:5001/city", text='London')
            mocker.get("http://service_3_api:5002/activity", text='Paintballing')
            mocker.post("http://service_4_api:5003/price", text='200') 
            response = self.client.get(url_for('index'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'The total cost of your holiday will be 200 GBP', response.data)

    # def test_service1(self):
    #     with requests_mock.Mocker() as mocker:
    #         mocker.get("http://service_2_api:5000/city", text='Milan')
    #         mocker.get("http://service_3_api:5000/activity", text='Surfing')
    #         mocker.post("http://service_4_api:5000/price", text='400') 
    #         response = self.client.get(url_for('index'))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertIn(b'The total cost of your holiday will be 400 GBP', response.data)