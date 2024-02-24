from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import CategorySerializer
from shop.models import Category


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для модели категории."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
