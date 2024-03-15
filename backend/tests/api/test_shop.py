import pytest
from rest_framework import status
from rest_framework.test import APIClient

from shop.models import Packing, Category


@pytest.mark.django_db
def test_add_product_auth_superuser_client(
        auth_superuser_client: APIClient, product_data: dict
) -> None:
    response = auth_superuser_client.post(
        '/api/products/', product_data, format='json'
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data.get('id') == product_data.get('id')
    assert response.data.get('name') == product_data.get('name')
    assert response.data.get('category') == product_data.get('category')
    assert (response.data.get('description')
            == product_data.get('description'))
    assert response.data.get('packing')
    for packing in response.data.get('packing'):
        assert packing.get('weight')
        assert isinstance(packing.get('weight'), int)
        assert (packing.get('price')
                == product_data.get('packing')[0].get('price'))
        assert packing.get('name')
    assert response.data.get('images')
    for image in response.data.get('images'):
        assert image.get('image')
        assert image.get('preview')
    assert response.data.get('created')
    assert response.data.get('updated')


@pytest.mark.django_db
@pytest.mark.parametrize(
    'client',
    (
        pytest.lazy_fixture('no_auth_client'),
        pytest.lazy_fixture('auth_client')
    ),
)
def test_add_product_auth_client(
        client: APIClient, product_data: dict[str, list[dict], int, bool]
) -> None:
    response = client.post('/api/products/', product_data, format='json')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
@pytest.mark.parametrize(
    'client',
    (
            pytest.lazy_fixture('no_auth_client'),
            pytest.lazy_fixture('auth_client'),
            pytest.lazy_fixture('auth_superuser_client')
    ),
)
def test_categories_get_detail(
        client: APIClient, create_category: Category
) -> None:
    """Проверка детальной информации категории."""
    fields_quantity = 2
    url = f'/api/categories/{create_category.slug}/'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, dict)
    assert len(response.data) == fields_quantity
    assert response.data.get('name') == create_category.name
    assert response.data.get('slug') == create_category.slug
    assert isinstance(response.data.get('slug'), str)
    assert isinstance(response.data.get('name'), str)


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
        client: APIClient, method: str, expected_status: status,
        data: dict, detail: bool, create_category: Category
) -> None:
    url = '/api/categories/'
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
def test_packing_get_list(
        client: APIClient, create_packing: Packing
) -> None:
    fields_objects = 1
    url = '/api/packing/'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)
    assert len(response.data) == fields_objects


@pytest.mark.django_db
@pytest.mark.parametrize(
    'client',
    (
            pytest.lazy_fixture('no_auth_client'),
            pytest.lazy_fixture('auth_client'),
            pytest.lazy_fixture('auth_superuser_client')
    ),
)
def test_packing_get_detail(
        client: APIClient, create_packing: Packing
) -> None:
    url = f'/api/packing/{create_packing.pk}/'
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, dict)
    assert response.data.get('name') == create_packing.name
    assert response.data.get('id') == create_packing.id
    assert response.data.get('weight') == create_packing.weight
    assert isinstance(response.data.get('weight'), int)
    assert isinstance(response.data.get('id'), int)
    assert isinstance(response.data.get('name'), str)


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
        client: Packing, method: str, expected_status: status,
        data: dict, detail: bool, create_packing: Packing
) -> None:
    url = '/api/packing/'
    if detail:
        url += f'{create_packing.pk}/'
    response = getattr(client, method)(url, data, format='json')
    assert response.status_code == expected_status
