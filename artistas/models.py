from django.db import models


class Generos(models.Model):
    nombre=models.CharField("genero", max_length=20)
    class Meta:
        verbose_name="Género"
        verbose_name_plural="Géneros"
    
    def _str_(self):
        return self.nombre

class Origen(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Artistas(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='artistas/')
    descripcion = models.TextField()
    genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    origen = models.ForeignKey(Origen, on_delete=models.SET_NULL, null=True) # Relación para el desplegable

    def __str__(self):
        return f"{self.nombre} de {self.origen}"
    