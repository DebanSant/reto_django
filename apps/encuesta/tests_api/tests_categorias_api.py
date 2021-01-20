from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

from apps.encuesta.models import CategoriaEncuesta


class TestUsers(APITestCase):

    def setUp(self):
        CategoriaEncuesta.objects.create(name="testname")

    def test_get_categorias(self):
        response = self.client.get('/api/categoria/')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["name"], "testname")

    def test_post_categorias(self):
        data = {
            "name": "CategoriaTest",
        }
        response = self.client.post('/api/categoria/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_categorias_details(self):
        response = self.client.get('/api/categoria/', kwargs={"pk": 1})
        self.assertEqual(response.data[0]['name'], 'testname')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_categorias_update(self):
        response = self.client.put('/api/categoria/1/',
                                   data={'name': 'testname-actualizado'})
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_categorias_delete(self):
        response = self.client.delete('/api/categoria/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
