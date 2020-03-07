"""videosearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .api import ObtainJSONWebEmailTokenSimple

admin.site.site_header = _('Administrador VideoSearch 2020')

# swagger_url = 'http://videosearch.dev.com'
swagger_url = ''

if settings.DEBUG:
    swagger_url = ''

SCHEMA_VIEW = get_schema_view(
    openapi.Info(
        title=_('VideoSearch API 2020'),
        default_version='v0.1',
        description=_('Documentación técnica de la API de VideoSearch 2020'),
        # terms_of_service="https://videosearch.com/",
        contact=openapi.Contact(email='info@videosearch.com'),
        license=openapi.License(name="A determinar"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    url=swagger_url,  # base url
)


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('health/', include('health_check.urls')),
    # Autenticación
    path(
        'auth/login/',
        ObtainJSONWebEmailTokenSimple.as_view(),
        name='token_obtain_pair',
    ),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # VIDEOSEARCH
    path('movies/', include('movies.urls')),
    # API docs
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        SCHEMA_VIEW.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'swagger/',
        SCHEMA_VIEW.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'redoc/',
        SCHEMA_VIEW.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = (
        [path('__debug__/', include(debug_toolbar.urls))]
        + urlpatterns
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )

