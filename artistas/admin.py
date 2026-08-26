from django.contrib import admin
from .models import Generos, Artistas

    
@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)
    list_display = ("nombre",)

@admin.register(Artistas)
class ArtistasAdmin(admin.ModelAdmin):
    list_display=("nombre","imagen","descripcion",)
    search_fields =("genero",) 
    list_filter = ("origen",)