"""
    Modelos para películas
"""
from django.db import models
from django.utils.translation import gettext as _


class Movie(models.Model):
    """Clase para películas"""

    #:Nombre de la película
    title = models.CharField(_('Título'), max_length=240)

    #: path to movie file
    file = models.FileField(_('Archivo'), upload_to='static', max_length=240)

    def __str__(self):
        """Redefinición del método str"""
        return f'{self.name}'

    class Meta:
        verbose_name = _('Película')
        verbose_name_plural = _('Películas')
