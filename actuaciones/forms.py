from django import forms

from .models import Actuacion, Escenario


class EscenarioForm(forms.ModelForm):
    class Meta:
        model = Escenario
        fields = ["nombre", "ubicacion", "capacidad"]


class ActuacionForm(forms.ModelForm):
    class Meta:
        model = Actuacion
        fields = ["artista", "escenario", "fecha", "hora_inicio", "duracion_minutos", "descripcion"]
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "hora_inicio": forms.TimeInput(attrs={"type": "time"}),
        }
