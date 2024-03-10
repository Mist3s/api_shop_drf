import pytest
from rest_framework import status


@pytest.mark.django_db
def test_register_user(user):
    assert user.data.get('first_name')
    assert user.data.get('last_name')
    assert user.data.get('username')
    assert user.data.get('email')
