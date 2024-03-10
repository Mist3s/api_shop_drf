import pytest
from rest_framework import status


@pytest.mark.django_db
def test_register_user(user, client):
    response = client.post('/api/users/', user)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data.get('first_name')
    assert response.data.get('last_name')
    assert response.data.get('username')
    assert response.data.get('email')
    assert response.data['username'] == user['username']


@pytest.mark.django_db
def test_login_user(user, client):
    client.post('/api/users/', user)
    response = client.post(
        '/api/token/login/',
        dict(
            email=user['email'],
            password=user['password']
        )
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.data.get('auth_token')
