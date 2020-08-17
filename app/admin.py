from django.contrib import admin
from .models import Categoria
from .models import Receita
from .models import Usuario

admin.site.register(Categoria)
admin.site.register(Receita)
admin.site.register(Usuario)