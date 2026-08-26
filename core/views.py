"""
Módulo de vistas para la aplicación 'core'.

Gestiona la página de inicio del festival y la información general para asistentes.
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

<<<<<<< HEAD
def inicio(request):
=======

def inicio(request: HttpRequest) -> HttpResponse:
    """
    Renderiza la página de inicio principal del festival.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.

    Returns:
        HttpResponse: Renderizado de la plantilla 'core/inicio.html'.
    """
>>>>>>> 8610b61c5daf21b48ecb3a014e26c22a73f2457b
    return render(request, "core/inicio.html")
