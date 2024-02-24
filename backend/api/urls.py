from django.urls import path, include
from rest_framework import routers

from .views import CategoryViewSet

v1_router = routers.DefaultRouter()

v1_router.register(
    'categories',
    CategoryViewSet,
    basename='categories'
)

urlpatterns = [
    path('', include(v1_router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
