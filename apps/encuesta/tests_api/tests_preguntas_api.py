from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

from apps.encuesta.models import Preguntas,Encuesta


class TestUsers(APITestCase):

    def setUp(self):
        encuesta = Encuesta.objects.create(name="encuestaTest")
        Preguntas.objects.create(description="testname",question_survey=encuesta)

    def test_get_preguntas(self):
        response = self.client.get('/api/encuesta/1/pregunta/')
        result = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["description"], "testname")
    def test_post_preguntas(self):
        data = {
            "description": "AlternativasTest",
        }
        response = self.client.post('/api/encuesta/1/pregunta/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_preguntas_details(self):
        response = self.client.get('/api/encuesta/1/pregunta/', kwargs={"pk": 1})
        self.assertEqual(response.data[0]['description'], 'testname')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_preguntas_update(self):
        response = self.client.put('/api/encuesta/1/pregunta/1/',
                                   data={'description': 'testdescription-actualizado'})
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_preguntas_delete(self):
        response = self.client.delete('/api/encuesta/1/pregunta/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

