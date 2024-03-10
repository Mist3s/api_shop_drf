import pytest
from rest_framework.test import APIClient

user_data = dict(
    username='username',
    email='test_user@test.ru',
    password='TestPassword1!',
    first_name='Test',
    last_name='User'
)


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user(client):
    response = client.post('/api/users/', user_data)
    return response


@pytest.fixture
def get_auth_token(client, user):
    response = client.post(
        '/api/token/login/',
        dict(
            email=user['email'],
            password=user_data['password']
        )
    )
    return response.data.get('auth_token')
