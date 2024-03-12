from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiExample
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status

from .serializers import CategorySerializer, ProductSerializer, PackingSerializer, ProductGetSerializer
from shop.models import Category, Product, Packing
from .permissions import IsAdminOrReadOnly


@extend_schema_view(
    list=extend_schema(
        summary="Получить список упаковок",
        description="Страница доступна всем пользователям.",
        examples=[
            OpenApiExample(
                "Packing example",
                description="Test example for the list packing",
                value=
                {
                    "id": 0,
                    "name": "Test packing",
                    "weight": 1
                },
                status_codes=[str(status.HTTP_200_OK)],
            ),
        ],
    ),
    retrieve=extend_schema(
        summary="Детальная информация упаковки",
        description="Страница доступна всем пользователям.",
        examples=[
            OpenApiExample(
                "Packing example",
                description="Test example for the packing",
                value=
                {
                    "id": 0,
                    "name": "Test packing",
                    "weight": 1
                },
                status_codes=[str(status.HTTP_200_OK)],
            ),
        ],
    ),
)
class PackingViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели категории."""
    queryset = Packing.objects.all()
    serializer_class = PackingSerializer
    permission_classes = (AllowAny,)


@extend_schema_view(
    list=extend_schema(
        summary="Получить список категорий",
        description="Страница доступна всем пользователям.",
        examples=[
            OpenApiExample(
                "Category example",
                description="Test example for the list category",
                value=
                {
                    "name": "Test category",
                    "slug": "test-category"
                },
                status_codes=[str(status.HTTP_200_OK)],
            ),
        ],
    ),
    retrieve=extend_schema(
        summary="Детальная информация категории",
        description="Страница доступна всем пользователям.",
        examples=[
            OpenApiExample(
                "Category example",
                description="Test example for the category",
                value=
                {
                    "name": "Test category",
                    "slug": "test-category"
                },
                status_codes=[str(status.HTTP_200_OK)],
            ),
        ],
    ),
)
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели категории."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


@extend_schema_view(
    list=extend_schema(
        summary="Получить список продуктов",
        description="Страница доступна всем пользователям.",
        responses={
            status.HTTP_200_OK: ProductGetSerializer
        }
    ),
    create=extend_schema(
        summary="Добавить продукт",
        description="Страница доступна администратору.",
        responses={
            status.HTTP_201_CREATED: ProductGetSerializer
        }
    ),
    retrieve=extend_schema(
        summary="Получить продукт",
        description="Страница доступна всем пользователям.",
        responses={
            status.HTTP_200_OK: ProductGetSerializer
        }
    ),
    partial_update=extend_schema(
        summary="Обновить продукт",
        description="Страница доступна администратору.",
        responses={
            status.HTTP_200_OK: ProductGetSerializer
        }
    ),
    destroy=extend_schema(
        summary="Удалить продукт",
        description="Страница доступна администратору."
    )
)
class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели продуктов"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = (IsAdminOrReadOnly,)
