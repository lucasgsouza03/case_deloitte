import json
from rest_framework.test import APITestCase

from user.models import User

# Create your tests here.

class UserUrlsTests(APITestCase):
    fixtures = ['./fixtures/db.json',]

    def setUp(self) -> None:
        data = {
            "email": "admin@email.com",
            "password": "admin"
        }
        response = self.client.post('/user/token/', data=json.dumps(data), content_type='application/json')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.json()['access'])

        return super().setUp()

    def test_get_token(self):
        data = {
            "email": "admin@email.com",
            "password": "admin"
        }
        response = self.client.post('/user/token/', data=json.dumps(data), content_type='application/json')

        assert response.status_code == 200

        assert response.json()['access']

        assert response.json()['access']

    def test_refresh_token(self):
        data = {
            "email": "admin@email.com",
            "password": "admin"
        }
        response_access = self.client.post('/user/token/', data=json.dumps(data), content_type='application/json')

        refresh = response_access.json()['refresh']

        refresh_refresh = {
            "refresh": refresh
        }

        response = self.client.post('/user/token/refresh/', data=json.dumps(refresh_refresh), content_type='application/json')

        assert response.status_code == 200

        assert response.json()['access']

    def test_register_user(self):

        data = {
            "email": "test@email.com",
            "password": "test_password",
            "password2": "test_password"
        }

        response = self.client.post('/user/register/', data=json.dumps(data), content_type='application/json')

        assert response.status_code == 201

        user_created = User.objects.get(id=response.json()['id'])
        
        assert user_created


