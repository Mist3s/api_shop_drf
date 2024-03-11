from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiExample
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework import status

from .serializers import CategorySerializer, ProductSerializer, PackingSerializer
from shop.models import Category, Product, Packing


@extend_schema_view(
    list=extend_schema(
        summary="Получить список упаковок",
        description="Страница доступна всем пользователям."
    ),
    retrieve=extend_schema(
        summary="Детальная информация упаковки",
        description="Страница доступна всем пользователям.",
        examples=[
            OpenApiExample(
                "Post example",
                description="Test example for the post",
                value=
                {
                    "name": "Test category",
                    "slug": "test-category",
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
