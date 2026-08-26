"""
Módulo de etiquetas y filtros de plantilla para la autenticación y permisos en 'core'.

Proporciona filtros personalizados para evaluar roles de usuario en las plantillas Django.
"""

from typing import Any
from django import template
from django.contrib.auth.models import AnonymousUser, User
from core.decorators import es_gestor

register = template.Library()


@register.filter(name="is_gestor")
def is_gestor(user: Any) -> bool:
    """
    Filtro de plantilla que evalúa si un usuario tiene permisos de gestor.

    Permite mostrar u ocultar elementos del menú o botones en el HTML:
        {% load auth_extras %}
        {% if request.user|is_gestor %}
            <a href="...">Crear Actuación</a>
        {% endif %}

    Args:
        user (User | AnonymousUser): Objeto de usuario obtenido habitualmente de request.user.

    Returns:
        bool: True si el usuario tiene rol de gestor, False en caso contrario.
    """
    return es_gestor(user)