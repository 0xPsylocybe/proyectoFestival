"""
Módulo de vistas para la aplicación 'actuaciones'.

Gestiona las operaciones CRUD para los modelos Escenario y Actuacion,
así como la visualización pública de la programación del festival.
Controla los permisos mediante el decorador @gestor_required.
"""

from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from core.decorators import gestor_required
from artistas.models import Artistas
from .forms import ActuacionForm, EscenarioForm
from .models import Actuacion, Escenario


def lista_escenarios(request: HttpRequest) -> HttpResponse:
    """
    Muestra el listado de todos los escenarios registrados en el festival.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.

    Returns:
        HttpResponse: Renderizado de la plantilla 'actuaciones/escenario_list.html'
            con la lista completa de escenarios.
    """
    # Obtenemos todos los escenarios ordenados según la Meta del modelo (por nombre)
    escenarios = Escenario.objects.all()
    return render(request, "actuaciones/escenario_list.html", {"escenarios": escenarios})


@gestor_required
def crear_escenario(request: HttpRequest) -> HttpResponse:
    """
    Permite a los usuarios con rol de gestor crear un nuevo escenario.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django (GET o POST).

    Returns:
        HttpResponse: Redirección al listado de escenarios si el formulario es válido,
            o renderizado de 'actuaciones/escenario_form.html' con el formulario.
    """
    # Instanciamos el formulario con datos POST si existen, o vacío si es GET
    form = EscenarioForm(request.POST or None)

    # Si la petición es POST y los datos son válidos, guardamos en la base de datos
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Escenario creado con éxito.")
        return redirect("actuaciones:lista_escenarios")

    return render(request, "actuaciones/escenario_form.html", {"form": form})


@gestor_required
def editar_escenario(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Permite modificar la información de un escenario existente.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.
        pk (int): Clave primaria (ID) del escenario a editar.

    Returns:
        HttpResponse: Redirección al listado tras guardar con éxito, o renderizado
            del formulario con los datos actuales del escenario.
    """
    # Buscamos el escenario o lanzamos un error 404 si no existe
    escenario = get_object_or_404(Escenario, pk=pk)
    
    # Vinculamos el formulario a la instancia existente
    form = EscenarioForm(request.POST or None, instance=escenario)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Escenario actualizado con éxito.")
        return redirect("actuaciones:lista_escenarios")

    return render(request, "actuaciones/escenario_form.html", {"form": form})


@gestor_required
def eliminar_escenario(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Gestiona la confirmación y eliminación de un escenario.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.
        pk (int): Clave primaria (ID) del escenario a eliminar.

    Returns:
        HttpResponse: Redirección al listado tras confirmar eliminación (POST),
            o plantilla de confirmación 'actuaciones/escenario_confirm_delete.html' (GET).
    """
    escenario = get_object_or_404(Escenario, pk=pk)
    
    # Solo procedemos a borrar si el usuario confirma mediante POST
    if request.method == "POST":
        escenario.delete()
        messages.success(request, "Escenario eliminado.")
        return redirect("actuaciones:lista_escenarios")

    return render(request, "actuaciones/escenario_confirm_delete.html", {"escenario": escenario})


def programacion(request: HttpRequest) -> HttpResponse:
    """
    Vista pública de la programación, con filtros por día, escenario y artista.

    Los filtros llegan como parámetros GET (fecha, escenario, artista) y se
    combinan entre sí. Usa select_related para cargar artista y escenario en una
    sola consulta.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.

    Returns:
        HttpResponse: Renderizado de 'actuaciones/programacion.html' con las
            actuaciones filtradas y las opciones de filtrado.
    """
    actuaciones = Actuacion.objects.select_related("artista", "escenario")

    fecha = request.GET.get("fecha")
    escenario_id = request.GET.get("escenario")
    artista_id = request.GET.get("artista")

    if fecha:
        actuaciones = actuaciones.filter(fecha=fecha)
    if escenario_id:
        actuaciones = actuaciones.filter(escenario_id=escenario_id)
    if artista_id:
        actuaciones = actuaciones.filter(artista_id=artista_id)

    contexto = {
        "actuaciones": actuaciones,
        "dias": Actuacion.objects.dates("fecha", "day"),
        "escenarios": Escenario.objects.all(),
        "artistas": Artistas.objects.all(),
        "filtro": {
            "fecha": fecha or "",
            "escenario": escenario_id or "",
            "artista": artista_id or "",
        },
    }
    return render(request, "actuaciones/programacion.html", contexto)


@gestor_required
def crear_actuacion(request: HttpRequest) -> HttpResponse:
    """
    Permite a los gestores programar una nueva actuación musical en el festival.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.

    Returns:
        HttpResponse: Redirección a la programación tras guardar con éxito,
            o renderizado de 'actuaciones/actuacion_form.html' con el formulario y posibles errores.
    """
    form = ActuacionForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Actuación programada con éxito.")
        return redirect("actuaciones:programacion")

    return render(request, "actuaciones/actuacion_form.html", {"form": form})


@gestor_required
def editar_actuacion(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Permite modificar los datos y horarios de una actuación existente.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.
        pk (int): Clave primaria (ID) de la actuación a modificar.

    Returns:
        HttpResponse: Redirección a la programación tras guardar, o plantilla
            con el formulario pre-rellenado.
    """
    actuacion = get_object_or_404(Actuacion, pk=pk)
    form = ActuacionForm(request.POST or None, instance=actuacion)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Actuación actualizada con éxito.")
        return redirect("actuaciones:programacion")

    return render(request, "actuaciones/actuacion_form.html", {"form": form})


@gestor_required
def eliminar_actuacion(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Gestiona la confirmación y eliminación de una actuación programada.

    Args:
        request (HttpRequest): Objeto de solicitud HTTP de Django.
        pk (int): Clave primaria (ID) de la actuación a eliminar.

    Returns:
        HttpResponse: Redirección a la programación tras confirmación (POST),
            o renderizado de 'actuaciones/actuacion_confirm_delete.html' (GET).
    """
    actuacion = get_object_or_404(Actuacion, pk=pk)
    
    if request.method == "POST":
        actuacion.delete()
        messages.success(request, "Actuación eliminada.")
        return redirect("actuaciones:programacion")

    return render(request, "actuaciones/actuacion_confirm_delete.html", {"actuacion": actuacion})
