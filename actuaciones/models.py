"""
Módulo de modelos para la aplicación 'actuaciones'.

Define los modelos de datos, QuerySets personalizados y managers para la gestión 
de escenarios y las actuaciones musicales del festival, incluyendo restricciones 
de unicidad, validaciones y métodos auxiliares de cálculo de horarios.
"""

from datetime import date, datetime, time, timedelta
from typing import Optional
from django.core.exceptions import ValidationError
from django.db import models


class Escenario(models.Model):
    """
    Representa un escenario o tarima física dentro del recinto del festival.

    Attributes:
        nombre (CharField): Nombre identificativo del escenario (ej. 'Escenario Principal').
        ubicacion (CharField): Ubicación física dentro del recinto del festival.
        capacidad (PositiveIntegerField): Capacidad máxima estimada de asistentes.
        creado_en (DateTimeField): Fecha y hora de creación del registro.
        actualizado_en (DateTimeField): Fecha y hora de la última modificación.
    """

    nombre = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Nombre del escenario",
        help_text="Nombre identificativo único para el escenario.",
    )
    ubicacion = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Ubicación en el recinto",
        help_text="Descripción de la ubicación (ej. 'Zona Norte', 'Junto al lago').",
    )
    capacidad = models.PositiveIntegerField(
        verbose_name="Capacidad máxima",
        help_text="Número máximo aproximado de personas que caben en la zona del escenario.",
    )
    creado_en = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación",
    )
    actualizado_en = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de actualización",
    )

    class Meta:
        verbose_name = "Escenario"
        verbose_name_plural = "Escenarios"
        ordering = ["nombre"]

    def __str__(self) -> str:
        """
        Retorna la representación textual del escenario.

        Returns:
            str: Nombre del escenario y su capacidad máxima.
        """
        return f"{self.nombre} (Capacidad: {self.capacidad})"


class ActuacionQuerySet(models.QuerySet):
    """
    QuerySet personalizado para el modelo Actuacion con métodos de filtrado especializados.
    """

    def para_fecha(self, fecha: date) -> "ActuacionQuerySet":
        """
        Filtra las actuaciones programadas para un día concreto.

        Args:
            fecha (date): Objeto fecha para filtrar.

        Returns:
            ActuacionQuerySet: QuerySet con las actuaciones del día.
        """
        return self.filter(fecha=fecha)

    def para_escenario(self, escenario_id: int) -> "ActuacionQuerySet":
        """
        Filtra las actuaciones que tendrán lugar en un escenario concreto.

        Args:
            escenario_id (int): Identificador del escenario.

        Returns:
            ActuacionQuerySet: QuerySet filtrado por escenario.
        """
        return self.filter(escenario_id=escenario_id)

    def para_artista(self, artista_id: int) -> "ActuacionQuerySet":
        """
        Filtra las actuaciones correspondientes a un artista concreto.

        Args:
            artista_id (int): Identificador del artista.

        Returns:
            ActuacionQuerySet: QuerySet filtrado por artista.
        """
        return self.filter(artista_id=artista_id)

    def con_relaciones(self) -> "ActuacionQuerySet":
        """
        Optimiza las consultas trayendo por adelantado artista y escenario (select_related).

        Returns:
            ActuacionQuerySet: QuerySet optimizado para vistas de listado y programación.
        """
        return self.select_related("artista", "escenario")


class Actuacion(models.Model):
    """
    Representa la presentación en vivo de un artista en un escenario y horario específicos.

    Attributes:
        artista (ForeignKey): Referencia al artista o grupo que realiza la actuación.
        escenario (ForeignKey): Escenario donde se llevará a cabo la presentación.
        fecha (DateField): Día en el que se celebra la actuación.
        hora_inicio (TimeField): Hora exacta a la que está programado el inicio del concierto.
        duracion_minutos (PositiveIntegerField): Duración estimada del concierto en minutos.
        descripcion (TextField): Detalles, notas o requisitos especiales de la actuación (opcional).
        creado_en (DateTimeField): Fecha y hora de creación del registro.
        actualizado_en (DateTimeField): Fecha y hora de la última modificación.
    """

    artista = models.ForeignKey(
        "artistas.Artistas",
        on_delete=models.CASCADE,
        related_name="actuaciones",
        verbose_name="Artista",
        help_text="Artista o grupo que actuará.",
    )
    escenario = models.ForeignKey(
        Escenario,
        on_delete=models.CASCADE,
        related_name="actuaciones",
        verbose_name="Escenario",
        help_text="Escenario donde tendrá lugar la actuación.",
    )
    fecha = models.DateField(
        verbose_name="Fecha de la actuación",
        help_text="Día en el que se llevará a cabo el concierto.",
    )
    hora_inicio = models.TimeField(
        verbose_name="Hora de inicio",
        help_text="Hora a la que comenzará la actuación.",
    )
    duracion_minutos = models.PositiveIntegerField(
        default=60,
        verbose_name="Duración (minutos)",
        help_text="Duración estimada de la actuación en minutos.",
    )
    descripcion = models.TextField(
        blank=True,
        verbose_name="Descripción / Notas",
        help_text="Información adicional sobre la actuación o requerimientos técnicos.",
    )
    creado_en = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación",
    )
    actualizado_en = models.DateTimeField(
        auto_now=True,
        verbose_name="Fecha de actualización",
    )

    # Manager personalizado a partir del QuerySet
    objects = ActuacionQuerySet.as_manager()

    class Meta:
        verbose_name = "Actuación"
        verbose_name_plural = "Actuaciones"
        ordering = ["fecha", "hora_inicio"]
        constraints = [
            models.UniqueConstraint(
                fields=["escenario", "fecha", "hora_inicio"],
                name="unique_actuacion_mismo_escenario_fecha_hora",
            )
        ]

    def __str__(self) -> str:
        """
        Retorna una representación en cadena legible de la actuación.

        Returns:
            str: Detalle formateado con el artista, escenario, fecha y hora.
        """
        return f"{self.artista} en {self.escenario.nombre} ({self.fecha} a las {self.hora_inicio.strftime('%H:%M')})"

    @property
    def hora_fin(self) -> time:
        """
        Calcula la hora estimada de finalización sumando la duración en minutos.

        Returns:
            time: Objeto de tipo datetime.time con la hora aproximada de finalización.
        """
        dt_inicio = datetime.combine(self.fecha, self.hora_inicio)
        dt_fin = dt_inicio + timedelta(minutes=self.duracion_minutos)
        return dt_fin.time()

    def clean(self) -> None:
        """
        Valida las reglas de negocio de la actuación antes de persistir en base de datos.
        
        Comprueba que no existan colisiones de hora de inicio en el mismo escenario y fecha.

        Raises:
            ValidationError: Si ya existe otra actuación programada a la misma hora, fecha y escenario.
        """
        super().clean()
        if self.escenario_id and self.fecha and self.hora_inicio:
            # Consulta para detectar colisiones en el mismo escenario, fecha y hora de inicio
            solapamientos = Actuacion.objects.filter(
                escenario=self.escenario,
                fecha=self.fecha,
                hora_inicio=self.hora_inicio,
            )
            # Excluimos la propia instancia si ya existe en la BD (caso de edición)
            if self.pk:
                solapamientos = solapamientos.exclude(pk=self.pk)

            if solapamientos.exists():
                raise ValidationError(
                    {
                        "hora_inicio": (
                            f"Ya existe una actuación programada en el escenario '{self.escenario.nombre}' "
                            f"el día {self.fecha} a las {self.hora_inicio.strftime('%H:%M')}."
                        )
                    }
                )
