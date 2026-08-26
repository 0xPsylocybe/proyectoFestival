"""
Módulo de administración para la aplicación 'actuaciones'.

Registra y personaliza las vistas de administración de Django para los modelos
Escenario y Actuacion, facilitando la gestión de conciertos en el panel de control.
"""

from django.contrib import admin
from .models import Actuacion, Escenario


class ActuacionInline(admin.TabularInline):
    """
    Permite visualizar y editar las actuaciones directamente dentro de la ficha de un escenario.
    """

    model = Actuacion
    extra = 1
    fields = ("artista", "fecha", "hora_inicio", "duracion_minutos")
    show_change_link = True


@admin.register(Escenario)
class EscenarioAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Escenario.
    """

    list_display = ("nombre", "ubicacion", "capacidad", "total_actuaciones")
    search_fields = ("nombre", "ubicacion")
    list_filter = ("capacidad",)
    inlines = [ActuacionInline]

    @admin.display(description="Total Actuaciones")
    def total_actuaciones(self, obj: Escenario) -> int:
        """
        Calcula el número total de actuaciones programadas en este escenario.

        Args:
            obj (Escenario): Instancia del escenario evaluado.

        Returns:
            int: Cantidad total de actuaciones asociadas.
        """
        return obj.actuaciones.count()


@admin.register(Actuacion)
class ActuacionAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Actuacion.
    """

    list_display = (
        "artista",
        "escenario",
        "fecha",
        "hora_inicio",
        "duracion_minutos",
        "hora_fin_display",
    )
    list_filter = ("fecha", "escenario", "hora_inicio")
    search_fields = ("artista__nombre", "escenario__nombre")
    date_hierarchy = "fecha"
    ordering = ("fecha", "hora_inicio")

    @admin.display(description="Hora Fin Aprox.")
    def hora_fin_display(self, obj: Actuacion) -> str:
        """
        Muestra la hora aproximada de fin formateada en la tabla del panel admin.

        Args:
            obj (Actuacion): Instancia de la actuación.

        Returns:
            str: Hora en formato HH:MM.
        """
        return obj.hora_fin.strftime("%H:%M")
