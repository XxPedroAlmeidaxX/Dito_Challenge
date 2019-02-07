import json

from django.test import TestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from data_treat_api.no_model.DataTreatEndpoint import DataTreatEndpointFactory


# Data Treat tests
class DataTreatTest(TestCase):

    # Class variables
    url = 'http://localhost:8000/data-treat/api/data-treat/'

    expected_response = {
      "timeline": [
        {
          "timestamp": "2016-10-02T11:37:31.2300892-03:00",
          "revenue": 120,
          "transaction_id": "3409340",
          "store_name": "BH Shopping",
          "products": [
            {
              "name": "Tenis Preto",
              "price": 120
            }
          ]
        },
        {
          "timestamp": "2016-09-22T13:57:31.2311892-03:00",
          "revenue": 250,
          "transaction_id": "3029384",
          "store_name": "Patio Savassi",
          "products": [
            {
              "name": "Camisa Azul",
              "price": 100
            },
            {
              "name": "Calça Rosa",
              "price": 150
            }
          ]
        }
      ]
    }

    def setUp(self):

        # Setting the Mock for the test
        DataTreatEndpointFactory.use_mock = True

    def test_data_treat_get(self):
        response = RequestsClient().get(self.url)
        response_result = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(json.dumps(response_result), json.dumps(self.expected_response))
