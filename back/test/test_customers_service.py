import json
import unittest
from flask import request, jsonify
from unittest.mock import Mock
from back.config import Config
from .base import BaseTestCase
import time

customer = {
    "identification":"560969601",
    "name": "Carlos Rojas",
    "address": "cll 10 81 b 51 bogota",
    "phone":"6433535",
    "mail":"Carlosr@hotmail.com"
}


customer_get = [{
    "identification":"560969601",
    "name": "Carlos Rojas",
    "address": "cll 10 81 b 51 bogota",
    "phone":"6433535",
    "mail":"Carlosr@hotmail.com"
}]


customer_update = {
    "identification":"560969601",
    "name": "Carlos",
    "address": "cll  51 bogota",
    "phone":"6435",
    "mail":"Carosr@hotmail.com"
}

info = json.dumps(customer)
info_update = json.dumps(customer_update)

URL_API = "http://127.0.0.1:5000"


class TestCustomersService(BaseTestCase):
    """Testing customers service"""

    def setUp(self):
        self.client.delete(URL_API + '/customers/' + customer['identification'])
        self.response = self.client.post(URL_API + '/customers', data=info, headers={'Content-Type': 'application/json'})

    def test_post_customer_response(self):
        """Ensure the service /customers route behaves correctly."""
        #response = self.client.post(URL_API + '/customers', data=info, headers={'Content-Type': 'application/json'})
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual(self.response.json, customer)

    def test_get_customers_response(self):
        """Ensure the service /customers route behaves correctly."""
        res = self.client.get(URL_API + '/customers',headers={'Content-Type': 'application/json'})
        customer = list(filter(lambda customer: customer['identification'] == '560969601', res.json))
        self.assertEqual(res.status_code, 200)
        self.assertListEqual(customer,customer_get)

    def test_get_customer_response(self):
        """Ensure the service /customers route behaves correctly."""
        response = self.client.get(URL_API + '/customers/' + customer['identification'],headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json, customer)
   
    def test_put_customer_response(self):
        """Ensure the service /customers route behaves correctly."""
        response = self.client.put(URL_API + '/customers/' + customer['identification'], data=info_update, headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json, customer_update)

    def test_delete_customer_response(self):
        """Ensure the service /customers route behaves correctly."""
        response = self.client.delete(URL_API + '/customers/' + customer['identification'])
        print(URL_API)
        print(response.json)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
