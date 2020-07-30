from django.forms import ModelForm
from .models import Categoria
from .models import Receita


class ReceitaForm(ModelForm):
    class Meta:
        model = Receita
        fields = ['nome', 'ingredientes', 'preparo', 'categoria']