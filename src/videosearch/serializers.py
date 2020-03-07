"""Modulo para definiar serializadores genéricos para el proyecto."""

from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_friendly_errors.mixins import FriendlyErrorMessagesMixin

USER = get_user_model()


class CustomJWTSimpleSerializer(
    FriendlyErrorMessagesMixin, TokenObtainPairSerializer
):
    """
    Serializador para la obtención de un token JWT para nuestra aplicación.
    En donde validamos los diferentes campos enviados y capturando cualquier
    error que se haya podido producir.
    """

    username_field = 'email'

    default_error_messages = {
        'no_active_account': _('No existe una cuenta con esas credenciales')
    }

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user_obj = USER.objects.filter(email=email).first()
        if user_obj is not None:
            credentials = {'username': user_obj.username, 'password': password}
            if user_obj.is_active is False:
                msg = _('Cuenta de usuario deshabilitada.')
                raise serializers.ValidationError(msg)
            user = authenticate(**credentials)
            if user:
                refresh = self.get_token(user)
                data = {}
                data['refresh'] = str(refresh)
                data['access'] = str(refresh.access_token)
                return data
            else:
                msg = _(
                    'No se puede iniciar sesión con las \
                        credenciales proporcionadas.'
                )
                raise serializers.ValidationError(msg)

        else:
            msg = _(
                'La cuenta con el correo electrónico especificado \
                    no existe.'
            )
            raise serializers.ValidationError(msg)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Añadimos la información que queremos pasar al JWT
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name

        return token
