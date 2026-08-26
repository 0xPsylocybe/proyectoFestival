"""
Configuración principal de rutas URL para el proyecto Festival.

Define el enrutamiento global conectando las aplicaciones 'core',
'artistas', 'actuaciones' y el panel de administración de Django.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from core.views import inicio

urlpatterns = [
    # Panel de administración de Django
    path("admin/", admin.site.urls),

    # Página principal
    path("", inicio, name="inicio"),

    # Rutas de las aplicaciones del proyecto
    path("", include("actuaciones.urls")),
    path("", include("artistas.urls")),
]

# Servir archivos estáticos y subidas de medios durante el desarrollo local
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
