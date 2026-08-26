"""
Módulo de formularios para la aplicación 'artistas'.

Define los ModelForms para la creación, edición y administración
de artistas y géneros musicales con widgets estilizados.
"""

from django import forms
from .models import Artistas, Generos


class ArtistasForms(forms.ModelForm):
    """
    Formulario para la gestión y registro de artistas y agrupaciones musicales.
    """

    class Meta:
        model = Artistas
        fields = [
            "nombre",
            "imagen",
            "descripcion",
            "origen",
            "generos",
        ]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nombre del artista o grupo",
                }
            ),
            "imagen": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Breve descripción o biografía...",
                }
            ),
            "origen": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "generos": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                }
            ),
        }


class GeneroForms(forms.ModelForm):
    """
    Formulario para la creación y edición de géneros musicales.
    """

    class Meta:
        model = Generos
        fields = [
            "nombre",
        ]
        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej: Rock, Indie, Techno",
                }
            ),
        }