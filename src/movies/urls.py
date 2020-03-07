"""
Endpoints para la API de ``movies``.
"""
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .api import MovieViewSet


router = DefaultRouter()
router.register('movies', MovieViewSet, basename='movies')

urlpatterns = [path('', include(router.urls))]
