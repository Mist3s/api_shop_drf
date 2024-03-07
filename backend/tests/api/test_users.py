import pytest


@pytest.mark.django_db
def test_register_user(user, client):
    response = client.post('/api/users/', user)
    data = response.data
    assert data['username'] == user['username']
