from django.forms import ModelForm
from django import forms
from .models import Categoria
from .models import Receita
from .models import Usuario


class ReceitaForm(ModelForm):
    class Meta:
        model = Receita
        fields = ['nome', 'ingredientes', 'preparo', 'categoria']


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'receita']
        widgets = {
            'senha': forms.PasswordInput(),
        }


class LoginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(widget=forms.PasswordInput)
