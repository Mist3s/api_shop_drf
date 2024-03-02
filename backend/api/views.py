from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import CategorySerializer, ProductSerializer, PackingSerializer
from shop.models import Category, Product, Packing


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
