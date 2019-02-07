from django.test import TestCase
from rest_framework import status
from rest_framework.test import RequestsClient

from autocomplete_api.models import User


# User tests
class UserTest(TestCase):

    # Class variables
    url = 'http://localhost:8000/autocomplete/api/user/'

    user_dakarai_id = 1
    user_dakarai_name = 'Dakarai Silva'
    user_dakarai_email = 'dakarai.silva@email.com'

    def setUp(self):

        # Setting start data
        User(id=self.user_dakarai_id, name=self.user_dakarai_name, email=self.user_dakarai_email).save()
        User(name='Dilermando Reis', email='dilermando.reis@email.com').save()
        User(name='Epaminondas Costa', email='epaminondas.costa@email.com').save()

    def asserts_user_get_id_result(self, user_id, user_name, user_email):
        response = RequestsClient().get(self.url + '{id}/'.format(id=user_id))
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['id'], user_id)
        self.assertEqual(response_data['name'], user_name)
        self.assertEqual(response_data['email'], user_email)

    def test_user_get(self):
        response = RequestsClient().get(self.url)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response_data), User.objects.count())

    def test_user_get_id(self):
        self.asserts_user_get_id_result(self.user_dakarai_id, self.user_dakarai_name, self.user_dakarai_email)

    def test_user_post(self):

        user_chopin_id = 4
        user_chopin_name = 'Frédéric Chopin'
        user_chopin_email = 'Ballade1inGminorOp23.email.com'

        response = RequestsClient().post(self.url, json={
            "name": user_chopin_name,
            "email": user_chopin_email
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.asserts_user_get_id_result(user_chopin_id, user_chopin_name, user_chopin_email)

    def test_user_put(self):
        user_dakarai_new_name = 'Dakarai Silva Costa'
        user_dakarai_new_email = 'dakarai.silva.costa@email.com'

        response = RequestsClient().put(self.url + '{id}/'.format(id=self.user_dakarai_id), json={
            "name": user_dakarai_new_name,
            "email": user_dakarai_new_email
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.asserts_user_get_id_result(self.user_dakarai_id, user_dakarai_new_name, user_dakarai_new_email)

    def test_user_patch(self):
        user_dakarai_new_name = 'Dakarai Silva Costa'

        response = RequestsClient().patch(self.url + '{id}/'.format(id=self.user_dakarai_id), json={
            "name": user_dakarai_new_name,
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.asserts_user_get_id_result(self.user_dakarai_id, user_dakarai_new_name, self.user_dakarai_email)

    def test_user_delete(self):
        response = RequestsClient().delete(self.url + '{id}/'.format(id=self.user_dakarai_id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = RequestsClient().get(self.url + '{id}/'.format(id=self.user_dakarai_id))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
