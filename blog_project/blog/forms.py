from django import forms
from .models import Articulo
from django.contrib.auth.models import User

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ('titulo', 'subtitulo', 'cuerpo', 'imagen', 'autor')