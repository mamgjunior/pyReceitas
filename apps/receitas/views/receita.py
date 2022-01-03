from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from receitas.models import Receita
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request, template_name='receitas/index.html'):
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)
    dados = {'receitas': receitas_por_pagina}
    return render(request, template_name, dados)


def receita(request, template_name='receitas/receita.html', pk=None):
    receita = get_object_or_404(Receita, pk=pk)
    dados = {'receita': receita}
    return render(request, template_name, dados)


def criar_receita(request, template_name='receitas/criar_receita.html'):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita(pessoa=user, 
            nome_receita=request.POST['nome_receita'],
            ingredientes=request.POST['ingredientes'],
            modo_preparo=request.POST['modo_preparo'],
            tempo_preparo=request.POST['tempo_preparo'],
            rendimento=request.POST['rendimento'],
            categoria=request.POST['categoria'],
            foto_receita=request.FILES['foto_receita'])
        receita.save()
        return redirect('usuarios:dashboard')
    else:
        return render(request, template_name)


def editar_receita(request, template_name='receitas/editar_receita.html', pk=None):
    receita = get_object_or_404(Receita, pk=pk)
    dados = {'receita': receita}
    return render(request, template_name, dados)


def atualizar_receita(request):
    if request.method == 'POST':
        receita = Receita.objects.get(pk=request.POST['receita_id'])
        receita.nome_receita = request.POST['nome_receita']
        receita.ingredientes = request.POST['ingredientes']
        receita.modo_preparo = request.POST['modo_preparo']
        receita.tempo_preparo = request.POST['tempo_preparo']
        receita.rendimento = request.POST['rendimento']
        receita.categoria = request.POST['categoria']

        if 'foto_receita' in request.FILES:
            receita.foto_receita  = request.FILES['foto_receita']
        
        receita.save()
        return redirect('usuarios:dashboard')


def deletar_receita(request, pk=None):
    receita = get_object_or_404(Receita, pk=pk)
    receita.delete()
    return redirect('usuarios:dashboard')
