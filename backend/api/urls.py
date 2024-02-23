from django.urls import path, include, re_path
from rest_framework import routers

v1_router = routers.DefaultRouter()

urlpatterns = [
    # path('api/', include('v1_router.urls', namespace='api_v1')),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
