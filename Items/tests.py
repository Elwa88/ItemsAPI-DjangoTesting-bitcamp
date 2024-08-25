from django.test import TestCase
from django.urls import reverse
from .models import Item
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class PublicItemTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_createItems(self):
        #post with valid price
        response =  self.client.post(reverse('public'),{"name":"Item1","price":15})
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

        #post with invalid price
        response1 =  self.client.post(reverse('public'),{"name":"Item1","price":-15})
        self.assertEqual(response1.status_code,status.HTTP_400_BAD_REQUEST)

    def test_listItems(self):
        response = self.client.get(reverse('public'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PrivateItemTests(TestCase):
    def setUp(self) :
        self.client = APIClient()
        self.user = User.objects.create(username='user',password = 'userpass')
        self.token =RefreshToken.for_user(self.user)

    def test_listPrivateItems_authorized(self):
        self.client.credentials(HTTP_AUTHORIZATION = f'Bearer {self.token.access_token}')
        response = self.client.get(reverse('private'))
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_listPrivateItems_unauthorized(self):
        response = self.client.get(reverse('private'))
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)