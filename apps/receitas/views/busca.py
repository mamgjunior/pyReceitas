from django.shortcuts import render
from receitas.models import Receita


def buscar(request, template_name='receitas/index.html'):
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        lista_receitas = lista_receitas.filter(nome_receita__icontains=request.GET['buscar'])

    dados = {'receitas' : lista_receitas}
    return render(request, template_name, dados)
