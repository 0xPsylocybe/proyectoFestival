from django.urls import path

from . import views

app_name = "actuaciones"

urlpatterns = [
    path("escenarios/", views.lista_escenarios, name="lista_escenarios"),
    path("escenarios/nuevo/", views.crear_escenario, name="crear_escenario"),
    path("escenarios/<int:pk>/editar/", views.editar_escenario, name="editar_escenario"),
    path("escenarios/<int:pk>/eliminar/", views.eliminar_escenario, name="eliminar_escenario"),

    path("programacion/", views.programacion, name="programacion"),
    path("actuaciones/nueva/", views.crear_actuacion, name="crear_actuacion"),
    path("actuaciones/<int:pk>/editar/", views.editar_actuacion, name="editar_actuacion"),
    path("actuaciones/<int:pk>/eliminar/", views.eliminar_actuacion, name="eliminar_actuacion"),
]
