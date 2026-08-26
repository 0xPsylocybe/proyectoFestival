from django import forms

from .models import Escenario


class EscenarioForm(forms.ModelForm):
    class Meta:
        model = Escenario
        fields = ["nombre", "ubicacion", "capacidad"]
