from django.db import models
from django_countries import CountryField


class Generos(models.Model):
    nombre=models.CharField("genero", max_length=20)
    class Meta:
        verbose_name="Género"
        verbose_name_plural="Géneros"
    
    def _str_(self):
        return self.nombre



class Artistas(models.Model):
    nombre = models.CharField("nombre",max_length=100)
    imagen = models.ImageField("imagen",upload_to='artistas/pfp')
    descripcion = models.CharField("descripcion", max_length=150)
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE,related_name="genero")
    origen = CountryField(blank_label='(Selecciona un país)')
    class Meta:
        verbose_name="Artista"
        verbose_name_plural="Artistas"
    
    def __str__(self):
        return f"{self.nombre} de {self.origen}"
    