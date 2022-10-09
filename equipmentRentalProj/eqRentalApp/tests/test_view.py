from urllib import response
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test import TestCase, Client
from django.urls import reverse
from base.serializers import UserSerializerWithToken
import json
from rest_framework.test import RequestsClient

class TestViews(TestCase):

    def setUp(self):
        password = "asd"
        test_user_password = "password"
        self.newUser_password = "NewUser"

        my_admin = User.objects.create_superuser('asd', 'asd@email.com', password)
        self.test_user = User.objects.create_user('user', 'user@email.com', test_user_password)

        serializer = UserSerializerWithToken(my_admin, many=False) #create token
        user_serializer = UserSerializerWithToken(self.test_user, many=False) #create token

        c = Client()
        self.c2 = Client()
        self.unathorized_user = Client()

        c.login(username=my_admin.username, password=password)
        self.c2.login(username=self.test_user.username, password=test_user_password)

        token = serializer.data['token']
        user_token = user_serializer.data['token']
        self.auth_headers = {'HTTP_AUTHORIZATION': 'Bearer {}'.format(token)}
        self.user_auth_headers = {'Authorization': 'Bearer {}'.format(user_token)}

        self.users = c.get('/users/', **self.auth_headers)
        self.response = c.get(reverse('users'))


    def test_RegisterUser(self):

        self.reponse2 = self.unathorized_user.post(reverse('register'), {"name": "new_User", "email": "newUser@email.com", "password": self.newUser_password})
        self.assertEquals(self.reponse2.data["username"], "newUser@email.com")
        self.assertEquals(self.reponse2.data["email"], "newUser@email.com")
        self.assertEquals(self.reponse2.data["name"], "new_User")
        self.assertEquals(self.reponse2.data["isAdmin"], False)