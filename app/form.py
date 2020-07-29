from django.forms import ModelForm
from .models import Categoria
from .models import Receita


class ReceitaForm(ModelForm):
    class Meta:
        model = Receita
        fields = ['nome', 'principal', 'ingredientes', 'preparo', 'categoria']