from django import forms
from .models import Artistas, Generos, Origen

class ArtistasForms(forms.ModelForm):
    class Meta:
        model=Artistas
        fields=[
            "nombre",
            "imagen",
            "descripcion",
            "origen",
            "genero"
        ]
    widgets={
        'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Nombre de artista'}),
        'imagen':forms.ImageField(attrs={'class':'form-control'}),
        'descripcion':forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción del artista'}),
        'origen': forms.Select(attrs={'class': 'form-select'}),
        'genero': forms.Select(attrs={'class': 'form-select'}),
    }

class GeneroForms(forms.ModelForm):
     class Meta:
            model=Generos
            fields=[
                "nombre",
                ]