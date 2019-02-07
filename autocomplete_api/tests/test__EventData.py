from django.test import TestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from autocomplete_api.models import EventData, User


# Event Data tests
class EventDataTest(TestCase):

    # Class variables
    url = 'http://localhost:8000/autocomplete/api/eventData/'
    user = None

    event_buy_food_id = 1
    event_buy_food = 'comprar comida'
    event_buy_food_datetime = '2016-09-22T17:57:31Z'

    def setUp(self):

        # Setting start data
        self.user = User(name='Dakarai Silva', email='dakarai.silva@email.com')
        self.user.save()

        EventData(id=self.event_buy_food_id, event=self.event_buy_food, dateTime=self.event_buy_food_datetime, user=self.user).save()
        EventData(event='comprar roupa cara', dateTime='2016-09-22T13:57:31', user=self.user).save()
        EventData(event='conserto de viola', dateTime='2016-10-22T13:57:31', user=self.user).save()

    def asserts_event_data_get_id_result(self, event_data_id, event_data, event_data_datetime):
        response = RequestsClient().get(self.url + '{id}/'.format(id=event_data_id))
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['id'], event_data_id)
        self.assertEqual(response_data['event'], event_data)
        self.assertEqual(response_data['dateTime'], event_data_datetime)
        self.assertEqual(response_data['user'], self.user.id)

    def test_event_data_get(self):
        response = RequestsClient().get(self.url)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response_data), EventData.objects.count())

    def test_event_data_get_id(self):
        self.asserts_event_data_get_id_result(self.event_buy_food_id, self.event_buy_food, self.event_buy_food_datetime)

    def test_event_data_post(self):

        event_car_rent_id = 4
        event_car_rent = 'aluguel de carro'
        event_car_rent_datetime = '2017-10-22T13:57:31Z'

        response = RequestsClient().post(self.url, json={
            "event": event_car_rent,
            "dateTime": event_car_rent_datetime,
            "user": self.user.id
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.asserts_event_data_get_id_result(event_car_rent_id, event_car_rent, event_car_rent_datetime)

    def test_event_data_put(self):
        event_buy_expensive_food = 'comprar comida cara'
        event_buy_expensive_food_datetime = '2017-09-22T17:57:31Z'

        response = RequestsClient().put(self.url + '{id}/'.format(id=self.event_buy_food_id), json={
            "event": event_buy_expensive_food,
            "dateTime": event_buy_expensive_food_datetime,
            "user": self.user.id
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.asserts_event_data_get_id_result(self.event_buy_food_id, event_buy_expensive_food, event_buy_expensive_food_datetime)

    def test_event_data_patch(self):
        event_buy_food_new_datetime = '2017-08-22T17:57:31Z'

        response = RequestsClient().patch(self.url + '{id}/'.format(id=self.event_buy_food_id), json={
            "dateTime": event_buy_food_new_datetime,
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.asserts_event_data_get_id_result(self.event_buy_food_id, self.event_buy_food, event_buy_food_new_datetime)

    def test_event_data_delete(self):
        response = RequestsClient().delete(self.url + '{id}/'.format(id=self.event_buy_food_id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = RequestsClient().get(self.url + '{id}/'.format(id=self.event_buy_food_id))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
