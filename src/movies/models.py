"""
    Modelos para películas
"""
from django.db import models
from django.utils.translation import gettext as _


class Movie(models.Model):
    """Clase para películas"""

    #:Nombre de la película
    name = models.CharField(_('Nombre'), max_length=240)

    #: path to movie file
    path = models.CharField(_('file path'), max_length=240)

    def __str__(self):
        """Redefinición del método str"""
        return f'{self.name}'

    class Meta:
        verbose_name = _('Película')
        verbose_name_plural = _('Películas')
