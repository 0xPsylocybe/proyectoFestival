"""
Módulo de modelos para la aplicación 'artistas'.

Define las entidades correspondientes a los géneros musicales y a los artistas
o grupos que participan en el festival, integrando compatibilidad con países
mediante django-countries.
"""

from django.db import models
from django_countries.fields import CountryField


class Generos(models.Model):
    """
    Representa un género o estilo musical (ej. Rock, Electrónica, Indie).

    Attributes:
        nombre (CharField): Nombre del género musical.
    """

    nombre = models.CharField(
        "Género",
        max_length=50,
        unique=True,
        help_text="Nombre descriptivo del género musical.",
    )

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ["nombre"]

    def __str__(self) -> str:
        """
        Retorna la representación textual del género musical.

        Returns:
            str: Nombre del género.
        """
        return self.nombre


class Artistas(models.Model):
    """
    Representa un artista, músico o banda participante en el festival.

    Attributes:
        nombre (CharField): Nombre artístico o nombre del grupo.
        imagen (ImageField): Fotografía o avatar promocional del artista.
        descripcion (TextField): Biografía resumida o descripción del artista.
        generos (ManyToManyField): Géneros musicales asociados al artista.
        origen (CountryField): País de procedencia del artista.
    """

    nombre = models.CharField(
        "Nombre",
        max_length=100,
        help_text="Nombre oficial del artista o agrupación.",
    )
    imagen = models.ImageField(
        "Imagen de perfil",
        upload_to="artistas/pfp",
        blank=True,
        null=True,
        help_text="Fotografía promocional del artista.",
    )
    descripcion = models.CharField(
        "Descripción",
        max_length=250,
        help_text="Breve descripción o biografía del artista.",
    )
    generos = models.ManyToManyField(
        Generos,
        related_name="artistas",
        verbose_name="Géneros musicales",
        help_text="Estilos o géneros asociados a este artista.",
    )
    origen = CountryField(
        blank_label="(Selecciona un país)",
        verbose_name="País de origen",
        help_text="Nacionalidad o país de procedencia del artista.",
    )

    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"
        ordering = ["nombre"]

    def __str__(self) -> str:
        """
        Retorna la representación textual del artista junto a su país de origen.

        Returns:
            str: Cadena formateada con el nombre del artista y su país.
        """
        if self.origen:
            return f"{self.nombre} ({self.origen.name})"
        return self.nombre


# Alias singular para compatibilidad con referencias en el proyecto
Artista = Artistas
Genero = Generos