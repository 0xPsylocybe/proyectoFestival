from django.shortcuts import render, get_object_or_404, redirect
from .models import Generos,Artistas
from .forms import ArtistasForms, GeneroForms
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#CRUD  de genero
@login_required
def genero_añadir(request):
    if request.method=="POST":
        formulario = GeneroForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Género creado con éxito")
        
        else:
            formulario=GeneroForms()
        return render (
            request,
            "artistas/genero_añadir.html",
            {
                "formulario":formulario
            }
        )

@login_required
def generos_lista(request):
    generos = Generos.objects.all()
    contexto = {
        "generos": generos
    }

    return render(
        request,
        "artistas/generos_lista.html",
        contexto
    )
    
@login_required
def genero_editar(request, pk):

    genero = get_object_or_404(Generos, pk=pk)

    if request.method == "POST":

        formulario = GeneroForms(
            request.POST,
            instance=genero
        )

        if formulario.is_valid():

            formulario.save()
            messages.success(request, "Género editado con éxito")
            return redirect("generos_lista")

    else:

        formulario = GeneroForms(instance=genero)

    return render(
        request,
        "artista/genero_añadir.html",
        {
            "formulario": formulario
        }
    )
          
@login_required
def genero_eliminar(request,pk):
    genero = get_object_or_404(
        Generos,
        pk=pk
    )
    if request.method == "POST":
        genero.delete()
        messages.ERROR(request,"Género eliminado")
        return redirect("genero_lista")

    return render(
        request,
        "artistas/genero_eliminar.html",
        {
            "genero": genero
        }
    )      

#CRUD de artistas
@login_required
def artista_añadir(request):
       if request.method=="POST":
            formulario = ArtistasForms(request.POST)
            if formulario.is_valid():
                formulario.save()
                messages.success(request, "Artista creado con éxito")
            
            else:
                formulario=ArtistasForms()
            return render (
                request,
                "artistas/añadir_artista.html",
                {
                    "formulario":formulario
                }
            )

@login_required
def artistas_lista(request):
    artistas = Artistas.objects.all()
    contexto = {
        "artistas": artistas
    }

    return render(
        request,
        "artistas/artistas_lista.html",
        contexto
    )

@login_required
def artista_editar(request,pk):

    artista = get_object_or_404(Artistas, pk=pk)
    if request.method == "POST":

        formulario = ArtistasForms(
            request.POST,
            instance=artista
        )

        if formulario.is_valid():

            formulario.save()
            messages.success(request, "Artista editado con éxito")
            return redirect("artistas/artistas_lista")

    else:

        formulario = ArtistasForms(instance=artista)

    return render(
        request,
        "artista/artista_añadir.html",
        {
            "formulario": formulario
        }
    )

@login_required
def artista_eliminar(request,pk):
    genero = get_object_or_404(
        Artistas,
        pk=pk
    )
    if request.method == "POST":
        genero.delete()
        messages.ERROR(request,"Artista eliminado")
        return redirect("artistas_lista")

    return render(
        request,
        "artistas/artistas_eliminar.html",
        {
            "genero": genero
        }
    )   

@login_required 
def detalle_artista(request,pk):
    
    artista=get_object_or_404(Artistas,pk=pk)
    contexto={
        "artista":artista
    }
    return render (
        request,
        "artistas/detalle_artista.html",
        contexto
    )