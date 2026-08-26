from django.shortcuts import get_object_or_404, redirect, render

from core.decorators import gestor_required
from .forms import EscenarioForm
from .models import Escenario


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
