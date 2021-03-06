from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.http import HttpResponse
from .models import Receita
from .form import ReceitaForm
from .form import LoginForm
from django.views.generic import CreateView, UpdateView, ListView
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, logout, login


# Views


def home(request):
    template_name = 'app/perfil.html'
    data = Receita.objects.all()
    busca = request.GET.get('busca')
    if busca:
        data = data.filter(nome__icontains=busca)

    context = {'receitas': data}
    return render(request, template_name, context)


def listagem(request):
    template_name = 'app/listagem.html'
    data = Receita.objects.all()
    busca = request.GET.get('busca')
    if busca:
        data = data.filter(nome__icontains=busca)
    context = {'receitas': data}
    return render(request, template_name, context)


class Buscar(ListView):
    model = Receita
    template_name = 'app/listagem.html'
    paginate_by = 10

    def get_queryset(self):
        queryset = super(Buscar, self).get_queryset()
        busca = self.request.GET.get('busca')
        if busca:
            queryset = queryset.filter(
                Q(nome__icontains=busca) |
                Q(ingredientes__icontains=busca)
            )
        return queryset


def receita_json(request, pk):
    ''' Retorna o produto, id e estoque. '''
    receita = Receita.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in receita]
    return JsonResponse({'data': data})


def nova_receita(request):
    data = {}
    form = ReceitaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')

    data['form'] = form
    return render(request, 'app/form.html', data)


def ver_receita(request, pk):
    template_name = 'app/visualizar.html'
    data = Receita.objects.filter(pk=pk)

    context = {'receitas': data}
    return render(request, template_name, context)


# Views Auth

def cadastro(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('lista')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'auth/cadastro.html', {'form_usuario': form_usuario})


def entrar(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('lista')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()
    return render(request, 'auth/login.html', {'form_login': form_login})


@login_required
def sair(request):
    logout(request)
    return HttpResponseRedirect('/login/login/')
