from django.forms import ModelForm
from django import forms
from .models import Categoria
from .models import Receita


class ReceitaForm(forms.Form):
    nome = forms.CharField(label='nome', max_length=100)
    ingredientes = forms.CharField(label='ingredientes', max_length=500)
    preparo = forms.CharField(label='preparo', max_length=500)
    categoria = forms.CharField(label='categoria', max_length=100)
    usuario = forms.CharField(label='usuario', max_length=100)


class LoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)
