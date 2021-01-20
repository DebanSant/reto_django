import json
from apps.users.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.users.api.serializers import *
from apps.users.models import  *


class TestUsers(APITestCase):

    def setUp(self):
        User.objects.create(email="test@email.com",username='testusername')

    def test_get_users(self):
        response = self.client.get('/api/usuario/')
        result = response.json()
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["username"],"testusername")

