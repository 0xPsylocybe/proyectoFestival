from django.contrib import admin
from .models import Generos, Artistas, Origen

@admin.register(Origen)
class OrigenAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)
    
@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ("nombre",)

@admin.register(Artistas)
class ArtistasAdmin(admin.ModelAdmin):
    list_display=("nombre","imagen","descripcion",)
    search_fields =("genero", "origen",) 