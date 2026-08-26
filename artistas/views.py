from django.shortcuts import render, get_object_or_404, redirect
from .models import Generos,Artistas,Origen
from .forms import 

@login_required
def genero_añadir(request):
    i