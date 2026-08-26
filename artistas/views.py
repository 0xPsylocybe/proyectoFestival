from django.shortcuts import render, get_object_or_404, redirect
from .models import Generos,Artistas,Origen
from .forms import ArtistasForm
from django.contrib.auth.decorators import login_required

@login_required
def genero_añadir(request):
    i