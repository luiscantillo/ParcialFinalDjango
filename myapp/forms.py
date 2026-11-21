from django import forms
from .models import Programa


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ["codigo", "nombre", "estado", "facultad"]
        labels = {
            "codigo": "Código",
            "nombre": "Nombre del programa",
            "estado": "Activo",
            "facultad": "Facultad",
        }
