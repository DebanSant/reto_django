from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

from apps.encuesta.models import Encuesta


class TestUsers(APITestCase):

    def setUp(self):
        Encuesta.objects.create(name="testname", description='testdescription')

    def test_get_encuesta(self):
        response = self.client.get('/api/encuesta/')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["name"], "testname")

    def test_post_encuestas(self):
        data = {
            "name": "EncuestaTest",
            "description": "EncuestadescriptionTest"
        }
        response = self.client.post('/api/encuesta/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_encuestas_details(self):
        response = self.client.get('/api/encuesta/', kwargs={"pk": 1})
        self.assertEqual(response.data[0]['name'], 'testname')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_encuestas_update(self):
        response = self.client.put('/api/encuesta/1/',
                                   data={'name': 'testname-actualizado', 'description': 'description_actualizada'})
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_encuestas_delete(self):
        response = self.client.delete('/api/encuesta/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
