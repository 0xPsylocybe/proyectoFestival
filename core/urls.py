from django.urls import path
from . import views


urlpatterns = [
    #core
    path("", views.inicio, name="inicio"),
    path("nosotros/", views.nosotros, name="nosotros"),]