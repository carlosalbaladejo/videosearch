"""
Serializadores para la app de Movies
"""

from rest_framework import serializers
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin

from .models import Movie


class MovieSerializer(
    FriendlyErrorMessagesMixin, serializers.ModelSerializer
):
    """Serializador básico para Movie."""

    class Meta:
        model = Movie
        fields = '__all__'
