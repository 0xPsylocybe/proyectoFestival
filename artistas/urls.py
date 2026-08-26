<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    #artistas
    path("artistas_lista", views.artistas_lista, name="artistas_lista"),
    path("detalle_artista/<int:pk>/", views.detalle_artista, name="detalle_artista"),
    path("añadir_artista",views.artista_añadir,name="añadir_artista"),
    path("<int:pk>/editar/",views.artista_editar,name="artista_editar"),
    path("<int:pk>/eliminar/",views.artista_eliminar,name="artista_eliminar"),
    #genero
    path("generos_lista", views.generos_lista, name="generos_lista"),
    path("añadir_genero",views.genero_añadir,name="añadir_genero"),
    path("<int:pk>/editar/",views.genero_editar,name="genero_editar"),
    path("<int:pk>/eliminar/",views.genero_eliminar,name="genero_eliminar"),
]
=======
"""
Módulo de enrutamiento URL para la aplicación 'artistas'.

Mapea las rutas URL con las vistas del catálogo de géneros y artistas del festival.
"""

from django.urls import path
from . import views

# Espacio de nombres de la aplicación
app_name = "artistas"

urlpatterns = [
    # Rutas para el CRUD de géneros musicales
    path("generos/", views.genero_lista, name="genero_lista"),
    path("generos/nuevo/", views.genero_añadir, name="genero_añadir"),
    path("generos/<int:pk>/editar/", views.genero_editar, name="genero_editar"),
    path("generos/<int:pk>/eliminar/", views.genero_eliminar, name="genero_eliminar"),

    # Rutas para el CRUD y detalle de artistas
    path("artistas/", views.artistas_lista, name="artistas_lista"),
    path("artistas/nuevo/", views.artista_añadir, name="artista_añadir"),
    path("artistas/<int:pk>/", views.detalle_artista, name="detalle_artista"),
    path("artistas/<int:pk>/editar/", views.artista_editar, name="artista_editar"),
    path("artistas/<int:pk>/eliminar/", views.artista_eliminar, name="artista_eliminar"),
]
>>>>>>> 8610b61c5daf21b48ecb3a014e26c22a73f2457b
