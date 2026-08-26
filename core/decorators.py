"""
Módulo de decoradores y utilidades de control de acceso para la aplicación 'core'.

Define funciones de comprobación de permisos para restringir el acceso a vistas
a usuarios que pertenezcan al grupo de 'Gestores' o sean superusuarios.
"""

from typing import Callable, Any
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User


def es_gestor(user: User) -> bool:
    """
    Comprueba si un usuario tiene privilegios de gestión en el festival.

    Args:
        user (User): Instancia del usuario autenticado que realiza la solicitud.

    Returns:
        bool: True si el usuario es superusuario o pertenece al grupo 'Gestores',
            False en caso contrario.
    """
    # Verificamos si es superusuario o si pertenece al grupo "Gestores"
    return user.is_authenticated and (user.is_superuser or user.groups.filter(name="Gestores").exists())


# Decorador de vista: redirige a la vista 'inicio' si el usuario no es gestor
gestor_required: Callable[..., Any] = user_passes_test(es_gestor, login_url="inicio")