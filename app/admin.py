from django.contrib import admin
from .models import Categoria
from .models import Receita

admin.site.register(Categoria)
admin.site.register(Receita)