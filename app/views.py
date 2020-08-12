from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Receita
from .form import ReceitaForm
from django.views.generic import CreateView, UpdateView, ListView
from django.db.models import Q


def home(request):
    data = {}
    return render(request, 'app/base.html', data)


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