from django.urls import path

from . import views

app_name = "actuaciones"

urlpatterns = [
    path("escenarios/", views.lista_escenarios, name="lista_escenarios"),
    path("escenarios/nuevo/", views.crear_escenario, name="crear_escenario"),
    path("escenarios/<int:pk>/editar/", views.editar_escenario, name="editar_escenario"),
    path("escenarios/<int:pk>/eliminar/", views.eliminar_escenario, name="eliminar_escenario"),
]
