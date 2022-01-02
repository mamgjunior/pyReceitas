from django.shortcuts import render, get_object_or_404
from . models import Receita


def index(request, template_name='index.html'):
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    dados = {'receitas': receitas}
    return render(request, template_name, dados)


def receita(request, template_name='receita.html', pk=None):
    receita = get_object_or_404(Receita, pk=pk)
    dados = {'receita': receita}
    return render(request, template_name, dados)


def buscar(request, template_name='index.html'):
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {'receitas' : lista_receitas}
    return render(request, template_name, dados)