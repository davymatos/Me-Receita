from django.forms import ModelForm
from django import forms
from .models import Categoria
from .models import Receita


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['nome', 'ingredientes', 'preparo', 'categoria', 'usuario']

        usuario = forms.CharField(widget=forms.Select())


class LoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)
