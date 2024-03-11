from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiExample
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status

from .serializers import CategorySerializer, ProductSerializer, PackingSerializer
from shop.models import Category, Product, Packing


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


class ProductViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели продуктов"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
