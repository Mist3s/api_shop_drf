from decimal import Decimal

import pytest
from rest_framework import status


@pytest.mark.django_db
def test_add_product_auth_superuser_client(auth_superuser_client, product_data):
    response = auth_superuser_client.post('/api/products/', product_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED, 'Expected status code 201.'
    assert response.data.get('id') == product_data.get('id'), 'Missing field "id".'
    assert response.data.get('name') == product_data.get('name'), 'Missing field "name".'
    assert response.data.get('category') == product_data.get('category'), 'Missing field "category".'
    assert (response.data.get('description')
            == product_data.get('description'), 'Missing field "description".')
    assert response.data.get('packing'), 'Missing field "packing".'
    for packing in response.data.get('packing'):
        assert packing.get('weight'), 'Missing field "weight" for "packing".'
        assert isinstance(packing.get('weight'), int), 'The field must be integer.'
        assert (packing.get('price') == product_data.get('packing')[0].get('price'),
                'Missing field "price" for "packing".')
        assert (isinstance(Decimal(packing.get('price')), Decimal),
                'The data in the field cannot be converted Decimal.')
        assert packing.get('name'), 'Missing field "name" for "packing".'
    assert response.data.get('images'), 'Missing field "images".'
    for image in response.data.get('images'):
        assert image.get('image'), 'Missing field "image" for "image".'
        assert image.get('preview'), 'Missing field "preview" for "image".'
    assert response.data.get('created'), 'Missing field "created".'
    assert response.data.get('updated'), 'Missing field "updated".'


@pytest.mark.django_db
@pytest.mark.parametrize(
    'client',
    (pytest.lazy_fixture('no_auth_client'), pytest.lazy_fixture('auth_client')),
)
def test_add_product_auth_client(client, product_data):
    response = client.post('/api/products/', product_data, format='json')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED, 'Only available superuser.'


@pytest.mark.django_db
@pytest.mark.parametrize(
    'client',
    (
            pytest.lazy_fixture('no_auth_client'),
            pytest.lazy_fixture('auth_client'),
            pytest.lazy_fixture('auth_superuser_client')
    ),
)
def test_categories_get_detail(client, create_category):
    url = f'/api/categories/{create_category.slug}/'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, dict)
    assert response.data.get('name') == create_category.name
    assert response.data.get('slug') == create_category.slug
    assert type(response.data.get('slug')) == str
    assert type(response.data.get('name')) == str


@pytest.mark.django_db
@pytest.mark.parametrize(
    'method, expected_status, data, detail',
    (
        ('post', status.HTTP_405_METHOD_NOT_ALLOWED,
         pytest.lazy_fixture('category_data'), False),
        ('put', status.HTTP_405_METHOD_NOT_ALLOWED,
         pytest.lazy_fixture('category_data'), True),
        ('patch', status.HTTP_405_METHOD_NOT_ALLOWED,
         pytest.lazy_fixture('category_data'), True),
        ('delete', status.HTTP_405_METHOD_NOT_ALLOWED,
         None, True)
    )
)
@pytest.mark.parametrize(
    'client',
    (
            pytest.lazy_fixture('no_auth_client'),
            pytest.lazy_fixture('auth_client'),
            pytest.lazy_fixture('auth_superuser_client')
    ),
)
def test_categories_method_not_available(
        client, method, expected_status, data, detail, create_category
):
    url = f'/api/categories/'
    if detail:
        url += f'{create_category.slug}/'
    response = getattr(client, method)(url, data, format='json')
    assert response.status_code == expected_status


@pytest.mark.django_db
@pytest.mark.parametrize(
    'client',
    (
            pytest.lazy_fixture('no_auth_client'),
            pytest.lazy_fixture('auth_client'),
            pytest.lazy_fixture('auth_superuser_client')
    ),
)
def test_packing_get_list(client, create_packing):
    url = '/api/packing/'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert len(response.data) == 1


@pytest.mark.django_db
@pytest.mark.parametrize(
    'client',
    (
            pytest.lazy_fixture('no_auth_client'),
            pytest.lazy_fixture('auth_client'),
            pytest.lazy_fixture('auth_superuser_client')
    ),
)
def test_packing_get_detail(client, create_packing):
    url = f'/api/packing/{create_packing.pk}/'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, dict)
    assert response.data.get('name') == create_packing.name
    assert response.data.get('id') == create_packing.id
    assert response.data.get('weight') == create_packing.weight
    assert type(response.data.get('weight')) == int
    assert type(response.data.get('id')) == int
    assert type(response.data.get('name')) == str


@pytest.mark.django_db
@pytest.mark.parametrize(
    'method, expected_status, data, detail',
    (
        ('post', status.HTTP_405_METHOD_NOT_ALLOWED,
         pytest.lazy_fixture('packing_data'), False),
        ('put', status.HTTP_405_METHOD_NOT_ALLOWED,
         pytest.lazy_fixture('packing_data'), True),
        ('patch', status.HTTP_405_METHOD_NOT_ALLOWED,
         pytest.lazy_fixture('packing_data'), True),
        ('delete', status.HTTP_405_METHOD_NOT_ALLOWED,
         None, True)
    )
)
@pytest.mark.parametrize(
    'client',
    (
            pytest.lazy_fixture('no_auth_client'),
            pytest.lazy_fixture('auth_client'),
            pytest.lazy_fixture('auth_superuser_client')
    ),
)
def test_packing_method_not_available(
        client, method, expected_status, data, detail, create_packing
):
    url = f'/api/packing/'
    if detail:
        url += f'{create_packing.pk}/'
    response = getattr(client, method)(url, data, format='json')
    assert response.status_code == expected_status

