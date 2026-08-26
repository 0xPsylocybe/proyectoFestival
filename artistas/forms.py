from django import forms
from .models import Artistas, Generos

class ArtistasForms(forms.ModelForm):
    class Meta:
        model=Artistas
        fields=[
            "nombre",
            "imagen",
            "descripcion",
            "origen",
            "generos"
        ]
    widgets={
        'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de artista'}),
        'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        'descripcion':forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción del artista'}),
        'origen': forms.Select(attrs={'class': 'form-select'}),
        'generos': forms.SelectMultiple(attrs={'class': 'form-select'}),
    }

class GeneroForms(forms.ModelForm):
     class Meta:
            model=Generos
            fields=[
                "nombre",
                ]