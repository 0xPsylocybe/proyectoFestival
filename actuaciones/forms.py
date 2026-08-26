"""
Módulo de formularios para la aplicación 'actuaciones'.

Define los ModelForms para la creación y edición de escenarios y actuaciones,
configurando widgets HTML5 nativos para fechas y horas.
"""

from django import forms
from .models import Actuacion, Escenario


class EscenarioForm(forms.ModelForm):
    """
    Formulario basado en el modelo Escenario para altas y modificaciones.
    """

    class Meta:
        model = Escenario
        fields = ["nombre", "ubicacion", "capacidad"]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Escenario Principal",
                }
            ),
            "ubicacion": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Zona Norte, junto al lago",
                }
            ),
            "capacidad": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: 5000",
                    "min": "1",
                }
            ),
        }


class ActuacionForm(forms.ModelForm):
    """
    Formulario basado en el modelo Actuacion para la programación de conciertos.
    
    Incluye widgets HTML5 de fecha ('date') y hora ('time') para mejorar
    la experiencia de usuario en navegadores modernos.
    """

    class Meta:
        model = Actuacion
        fields = [
            "artista",
            "escenario",
            "fecha",
            "hora_inicio",
            "duracion_minutos",
            "descripcion",
        ]
        widgets = {
            "artista": forms.Select(attrs={"class": "form-select"}),
            "escenario": forms.Select(attrs={"class": "form-select"}),
            "fecha": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "hora_inicio": forms.TimeInput(attrs={"type": "time", "class": "form-control"}),
            "duracion_minutos": forms.NumberInput(attrs={"class": "form-control", "min": "1"}),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Notas técnicas o comentarios sobre la actuación (opcional)...",
                }
            ),
        }
