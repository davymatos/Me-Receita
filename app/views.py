from django.shortcuts import render, redirect
from .models import Receita
from .form import ReceitaForm
from django.db.models import Q


def listagem(request):
    busca = request.GET.get("busca")
    if busca:
        data = Receita.objects.filter(
            Q(nome=busca) |
            Q(ingredientes=busca)
        ).distinct()
    else:
        data = {'receitas': Receita.objects.all()}
    return render(request, 'app/listagem.html', data)


def buscar(request, nome):
    data = {}
    receita = Receita.objects.get(nome=nome)
    form = ReceitaForm(request.POST or None, instance=receita)

    if form.is_valid():
        return redirect('lista')

    data['form'] = form
    data['receita'] = receita
    return render(request, 'app/form.html', data)


def nova_receita(request):
    data = {}
    form = ReceitaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')

    data['form'] = form
    return render(request, 'app/form.html', data)
