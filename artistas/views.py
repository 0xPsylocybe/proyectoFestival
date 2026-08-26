"""
Módulo de vistas para la aplicación 'artistas'.

Implementa las operaciones CRUD para los géneros musicales y para los artistas
participantes en el festival, incluyendo la visualización de la ficha de detalle.
"""

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ArtistasForms, GeneroForms
from .models import Artistas, Generos


# ==============================================================================
# CRUD de Géneros Musicales
# ==============================================================================

@login_required
def genero_añadir(request: HttpRequest) -> HttpResponse:
    """
    Permite a los usuarios autenticados crear un nuevo género musical.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.

    Returns:
        HttpResponse: Redirección al listado de géneros tras la creación exitosa,
            o renderizado del formulario en 'artistas/genero_añadir.html'.
    """
    if request.method == "POST":
        # Procesamos los datos enviados por el usuario
        formulario = GeneroForms(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Género creado con éxito")
            return redirect("artistas:genero_lista")
    else:
        # Petición GET: formulario en blanco
        formulario = GeneroForms()

    return render(
        request,
        "artistas/genero_añadir.html",
        {"formulario": formulario},
    )



def genero_lista(request: HttpRequest) -> HttpResponse:
    """
    Muestra la lista de todos los géneros musicales registrados.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.

    Returns:
        HttpResponse: Renderizado de la plantilla 'artistas/generos_lista.html'
            con el catálogo de géneros.
    """
    generos = Generos.objects.all()
    contexto = {"generos": generos}

    return render(
        request,
        "artistas/generos_lista.html",
        contexto,
    )


@login_required
def genero_editar(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Permite editar la denominación de un género musical existente.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.
        pk (int): Clave primaria (ID) del género a modificar.

    Returns:
        HttpResponse: Redirección al listado tras guardar, o renderizado
            de la plantilla de edición con los datos del género.
    """
    genero = get_object_or_404(Generos, pk=pk)

    if request.method == "POST":
        # Vinculamos datos POST a la instancia existente
        formulario = GeneroForms(request.POST, instance=genero)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Género editado con éxito")
            return redirect("artistas:genero_lista")
    else:
        formulario = GeneroForms(instance=genero)

    return render(
        request,
        "artistas/genero_añadir.html",
        {"formulario": formulario},
    )


@login_required
def genero_eliminar(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Gestiona la confirmación y eliminación de un género musical.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.
        pk (int): Clave primaria (ID) del género a eliminar.

    Returns:
        HttpResponse: Redirección al listado tras borrar (POST), o renderizado
            de la confirmación en 'artistas/genero_eliminar.html' (GET).
    """
    genero = get_object_or_404(Generos, pk=pk)

    if request.method == "POST":
        genero.delete()
        messages.error(request, "Género eliminado")
        return redirect("artistas:genero_lista")

    return render(
        request,
        "artistas/genero_eliminar.html",
        {"genero": genero},
    )


# ==============================================================================
# CRUD de Artistas
# ==============================================================================

@login_required
def artista_añadir(request: HttpRequest) -> HttpResponse:
    """
    Permite añadir un nuevo artista o grupo musical al catálogo del festival.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django con archivos (request.FILES).

    Returns:
        HttpResponse: Redirección al listado de artistas tras guardar,
            o renderizado de 'artistas/añadir_artista.html' con el formulario.
    """
    if request.method == "POST":
        # Incluimos request.FILES para soportar la subida de imagen de perfil
        formulario = ArtistasForms(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Artista creado con éxito")
            return redirect("artistas:artistas_lista")
    else:
        formulario = ArtistasForms()

    return render(
        request,
        "artistas/añadir_artista.html",
        {"formulario": formulario},
    )


def artistas_lista(request: HttpRequest) -> HttpResponse:
    """
    Muestra el listado de todos los artistas participantes en el festival.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.

    Returns:
        HttpResponse: Renderizado de 'artistas/artistas_lista.html' con la lista de artistas.
    """
    # Obtenemos los artistas junto con sus géneros precargados
    artistas = Artistas.objects.prefetch_related("generos").all()
    contexto = {"artistas": artistas}

    return render(
        request,
        "artistas/artistas_lista.html",
        contexto,
    )


@login_required
def artista_editar(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Permite modificar los datos, fotografía y géneros de un artista existente.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.
        pk (int): Clave primaria (ID) del artista a modificar.

    Returns:
        HttpResponse: Redirección al listado tras guardar, o renderizado
            de la plantilla de edición.
    """
    artista = get_object_or_404(Artistas, pk=pk)

    if request.method == "POST":
        # Se incluye request.FILES para actualizar la imagen si se sube una nueva
        formulario = ArtistasForms(request.POST, request.FILES, instance=artista)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Artista editado con éxito")
            return redirect("artistas:artistas_lista")
    else:
        formulario = ArtistasForms(instance=artista)

    return render(
        request,
        "artistas/artista_añadir.html",
        {"formulario": formulario},
    )


@login_required
def artista_eliminar(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Gestiona la confirmación y eliminación de un artista.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.
        pk (int): Clave primaria (ID) del artista a eliminar.

    Returns:
        HttpResponse: Redirección al listado tras borrar (POST), o renderizado
            de la plantilla de confirmación en 'artistas/artistas_eliminar.html'.
    """
    artista = get_object_or_404(Artistas, pk=pk)

    if request.method == "POST":
        artista.delete()
        messages.error(request, "Artista eliminado")
        return redirect("artistas:artistas_lista")

    return render(
        request,
        "artistas/artistas_eliminar.html",
        {"genero": artista},
    )



def detalle_artista(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Muestra la ficha detallada de un artista específico y sus actuaciones programadas.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.
        pk (int): Clave primaria (ID) del artista a consultar.

    Returns:
        HttpResponse: Renderizado de 'artistas/detalle_artista.html' con los datos del artista.
    """
    artista = get_object_or_404(Artistas.objects.prefetch_related("generos", "actuaciones"), pk=pk)
    contexto = {"artista": artista}

    return render(
        request,
        "artistas/detalle_artista.html",
        contexto,
    )