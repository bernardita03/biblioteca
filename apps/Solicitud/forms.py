from django import forms
from .models import Solicitud
 
class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['titulo', 'autor', 'año']
 
        labels = {
            'titulo': 'Titulo del libro',
            'autor': 'Nombre autor',
            'año': 'Año de publicacion',
 
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'año': forms.TextInput(attrs={'class': 'form-control'}),
           
        }
