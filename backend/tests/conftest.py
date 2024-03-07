import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return dict(
        username='test_user',
        email='test_user@test.ru',
        password='Tes!tUs!er321!',
        first_name='Test',
        last_name='User'

    )
