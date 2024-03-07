import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_register_user():
    payload = dict(
        username='test_user',
        email='test_user@test.ru',
        password='Tes!tUs!er321!',
        first_name='Test',
        last_name='User'

    )
    response = client.post('/api/users/', payload)
    data = response.data
    assert data['username'] == payload['username']
