from .models import Libro
from django import forms

class LibroForm(forms.ModelForm):
    

    class Meta:
        model = Libro
        fields = (
            'fotografia',
            'autor',
            'titulo',
            'categoria'
        )
        labels = {
            'fotografia':'Fotografia',
            'autor':'Autor',
            'titulo':'Titulo',
            'categoria':'Categoria'
        }
        widgets = {
            # 'fotografia':forms.FileInput(attrs={'class':'form-control','type':'file'}),
            'autor':forms.TextInput(attrs={'class':'form-control'}),
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(choices="CATEGORIAS", attrs={'class':'form-control'}),
        }