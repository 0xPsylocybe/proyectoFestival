from django.shortcuts import get_object_or_404, redirect, render

from core.decorators import gestor_required
from .forms import ActuacionForm, EscenarioForm
from .models import Actuacion, Escenario


def lista_escenarios(request):
    escenarios = Escenario.objects.all()
    return render(request, "actuaciones/escenario_list.html", {"escenarios": escenarios})


@gestor_required
def crear_escenario(request):
    form = EscenarioForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("actuaciones:lista_escenarios")
    return render(request, "actuaciones/escenario_form.html", {"form": form})


@gestor_required
def editar_escenario(request, pk):
    escenario = get_object_or_404(Escenario, pk=pk)
    form = EscenarioForm(request.POST or None, instance=escenario)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("actuaciones:lista_escenarios")
    return render(request, "actuaciones/escenario_form.html", {"form": form})


@gestor_required
def eliminar_escenario(request, pk):
    escenario = get_object_or_404(Escenario, pk=pk)
    if request.method == "POST":
        escenario.delete()
        return redirect("actuaciones:lista_escenarios")
    return render(request, "actuaciones/escenario_confirm_delete.html", {"escenario": escenario})


def programacion(request):
    actuaciones = Actuacion.objects.select_related("artista", "escenario")
    return render(request, "actuaciones/programacion.html", {"actuaciones": actuaciones})


@gestor_required
def crear_actuacion(request):
    form = ActuacionForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("actuaciones:programacion")
    return render(request, "actuaciones/actuacion_form.html", {"form": form})


@gestor_required
def editar_actuacion(request, pk):
    actuacion = get_object_or_404(Actuacion, pk=pk)
    form = ActuacionForm(request.POST or None, instance=actuacion)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("actuaciones:programacion")
    return render(request, "actuaciones/actuacion_form.html", {"form": form})


@gestor_required
def eliminar_actuacion(request, pk):
    actuacion = get_object_or_404(Actuacion, pk=pk)
    if request.method == "POST":
        actuacion.delete()
        return redirect("actuaciones:programacion")
    return render(request, "actuaciones/actuacion_confirm_delete.html", {"actuacion": actuacion})
