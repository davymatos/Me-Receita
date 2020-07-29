from django.shortcuts import render, redirect
from .models import Receita
from .form import ReceitaForm


def listagem(request):
    data = {'receitas': Receita.objects.all()}
    return render(request, 'app/listagem.html', data)


def nova_receita(request):
    data = {}
    form = ReceitaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista')

    data['form'] = form
    return render(request, 'app/form.html', data)