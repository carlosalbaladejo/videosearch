"""Modulo para definir vistar genéricas para el proyecto"""

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomJWTSimpleSerializer


class ObtainJSONWebEmailTokenSimple(TokenObtainPairView):
    """
    Vista de la API que mediante un método POST recibe un email y
    una contraseña de usuario, devolviendo un token JWT que se
    puede utilizar para realizar peticiones autenticadas a la API.
    """

    serializer_class = CustomJWTSimpleSerializer
