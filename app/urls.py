from django.urls import path
from . import views

urlpatterns = [
    path('', views.listagem, name='lista'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/login/', views.entrar, name='login'),
]
