from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet, ProductViewSet

v1_router = routers.DefaultRouter()

v1_router.register(
    'categories',
    CategoryViewSet,
    basename='categories'
)
v1_router.register(
    'products',
    ProductViewSet,
    basename='products'
)

urlpatterns = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
