import pytest
from rest_framework import status


@pytest.mark.django_db
def test_add_product(auth_client, product_data):
    response = auth_client.post('/api/products/', product_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data.get('id') == product_data.get('id')
    assert response.data.get('name') == product_data.get('name')
    assert response.data.get('category') == product_data.get('category')
    assert response.data.get('description') == product_data.get('description')
    assert response.data.get('packing')
    assert response.data.get('images')
    assert response.data.get('created')
    assert response.data.get('updated')
    assert response.data.get('available') == True


@pytest.mark.django_db
@pytest.mark.parametrize(
    'method, expected_status, data',
    (
        ('post', status.HTTP_405_METHOD_NOT_ALLOWED, pytest.lazy_fixture('category_data')),
        ('get', status.HTTP_200_OK, None)
    ),
)
def test_add_category_and_list(method, auth_client, expected_status, data, create_category):
    response = getattr(auth_client, method)(
        '/api/categories/', data
    )
    assert response.status_code == expected_status
    if response.request.get('REQUEST_METHOD') == 'GET':
        assert isinstance(response.data, list)
        assert response.data[0]['slug'] == create_category.slug
        assert response.data[0]['name'] == create_category.name

