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