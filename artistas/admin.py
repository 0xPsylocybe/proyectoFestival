"""
Módulo de administración para la aplicación 'artistas'.

Registra y personaliza las vistas del panel de control de Django para
los modelos Generos y Artistas.
"""

from django.contrib import admin
from .models import Artistas, Generos


@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Generos.
    """

    list_display = ("nombre", "total_artistas")
    search_fields = ("nombre",)
    ordering = ("nombre",)

    @admin.display(description="Total Artistas")
    def total_artistas(self, obj: Generos) -> int:
        """
        Calcula el número de artistas asociados a este género musical.

        Args:
            obj (Generos): Instancia del género evaluado.

        Returns:
            int: Cantidad de artistas vinculados.
        """
        return obj.artistas.count()


@admin.register(Artistas)
class ArtistasAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Artistas.
    """

    list_display = ("nombre", "origen", "descripcion", "mostrar_generos")
    search_fields = ("nombre", "descripcion", "generos__nombre")
    list_filter = ("origen", "generos")
    ordering = ("nombre",)

    @admin.display(description="Géneros")
    def mostrar_generos(self, obj: Artistas) -> str:
        """
        Devuelve una lista separada por comas de los géneros del artista.

        Args:
            obj (Artistas): Instancia del artista evaluado.

        Returns:
            str: Nombres de los géneros asociados concatenados.
        """
        return ", ".join(g.nombre for g in obj.generos.all())