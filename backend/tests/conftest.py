import pytest
from rest_framework.test import APIClient

from shop.models import Packing, Category


@pytest.fixture
def user_data():
    return dict(
        username='username',
        email='test_user@test.ru',
        password='TestPassword1!',
        first_name='Test',
        last_name='User'
    )


@pytest.fixture
def category_data():
    return dict(
        name='category',
        slug='category'
    )


@pytest.fixture
def image_data():
    return dict(
        image=(
            'data:image/gif;base64,R0lGODlhBwAKAMIEAICAgJmZmbOzs/f39///////'
            '/////////yH5BAEKAAcALAAAAAAHAAoAAAMWSDPUGoE5AaIj1M4qMW+ZFDYD1ClnAgA7'
        ),
        preview=True
    )


@pytest.fixture
def packing_data():
    return dict(
        name='packing',
        weight=1
    )


@pytest.fixture
def create_packing():
    packing = Packing.objects.create(name='packing_1', weight=1)
    return packing


@pytest.fixture
def create_category():
    category = Category.objects.create(name='category-1', slug='category-1')
    return category


@pytest.fixture
def product_data(image_data, create_packing, create_category):
    return dict(
        category=create_category.pk,
        name='Product',
        slug='product',
        description='Test product!',
        packing=[dict(id=create_packing.pk, price=100),],
        images=[image_data,]
    )


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user(client, user_data):
    response = client.post('/api/users/', user_data)
    print(response)
    return response


@pytest.fixture
def auth_client(client, user_data):
    response = client.post(
        '/api/token/login/',
        dict(
            email=user_data['email'],
            password=user_data['password']
        )
    )
    token = response.data.get('auth_token')
    client.credentials(Authorization=f'Token {token}')
    return client
