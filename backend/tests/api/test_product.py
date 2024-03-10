import pytest
from rest_framework import status


@pytest.mark.django_db
def test_add_product(auth_client, product_data):
    response = auth_client.post('/api/products/', product_data, format='json')
    print(response.data)
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
