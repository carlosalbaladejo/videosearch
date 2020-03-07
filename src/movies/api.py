"""Colección de vistas para películas"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    """Colección de endpoints para la gestión de residuos."""

    queryset = Movie.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ('title')
    ordering_fields = ('title')
    serializer_class = MovieSerializer
