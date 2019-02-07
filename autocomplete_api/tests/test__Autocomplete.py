from django.test import TestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from autocomplete_api.models import EventData, User


# Autocomplete tests
class AutocompleteTest(TestCase):

    # Class variables
    url = 'http://localhost:8000/autocomplete/api/autocomplete/'

    most_used_event_1 = 'comprar comida'
    most_used_event_2 = 'contas pagas'

    def setUp(self):

        # Setting start data
        user = User(name='Dakarai Silva', email='dakarai.silva@email.com')
        user.save()

        EventData(event=self.most_used_event_1, dateTime='2016-09-22T17:57:31', user=user).save()
        EventData(event=self.most_used_event_1, dateTime='2017-10-22T17:57:31', user=user).save()
        EventData(event=self.most_used_event_1, dateTime='2018-10-22T17:57:31', user=user).save()
        EventData(event='comprar roupa cara', dateTime='2016-09-22T13:57:31', user=user).save()
        EventData(event='comprar roupa cara 2', dateTime='2016-09-22T13:57:31', user=user).save()
        EventData(event='conserto de viola', dateTime='2016-10-22T13:57:31', user=user).save()
        EventData(event=self.most_used_event_2, dateTime='2016-10-22T13:57:31', user=user).save()
        EventData(event=self.most_used_event_2, dateTime='2016-11-22T13:57:31', user=user).save()
        EventData(event='random', dateTime='2016-10-22T13:57:31', user=user).save()

    # Makes a get request to autocomplete route using the passed parameters on querystring
    def autocomplete_get(self, event_param, **kwarg):
        query_params = '?event={event_param}'.format(event_param=event_param)

        if 'limit' in kwarg:
            query_params += '& limit = {limit}'.format(limit=kwarg['limit'])

        return RequestsClient().get(self.url + query_params)

    def test_autocomplete_get_default_limit(self):
        default_limit = 5
        event_param = 'co'

        response = self.autocomplete_get(event_param)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response_data), default_limit)

        for item in response_data:
            if not item.startswith(event_param):
                self.assertTrue(False)  # Do not have assert fail o(╥﹏╥)

    def test_autocomplete_get_with_limit(self):
        limit = 2
        event_param = 'co'

        response = self.autocomplete_get(event_param, limit=limit)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response_data), limit)
        self.assertEqual(response_data[0], self.most_used_event_1)
        self.assertEqual(response_data[1], self.most_used_event_2)

