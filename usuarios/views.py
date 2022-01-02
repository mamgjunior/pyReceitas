from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from receitas.models import Receita
from .utils import campo_vazio, senhas_nao_sao_iguais

def dashboard(request, template_name='usuarios/dashboard.html'):
    if request.user.is_authenticated:
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita').filter(pessoa=id)
        dados = {'receitas' : receitas}
        return render(request, template_name, dados)
    else:
        return redirect('receitas:index')


def login(request, template_name='usuarios/login.html'):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco.')
            return redirect('usuarios:login')

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Login realizado com sucesso')
                return redirect('usuarios:dashboard')
        else:
            return redirect('usuarios:login')
    else:
        return render(request, template_name)


def logout(request):
    auth.logout(request)
    return redirect('receitas:index')


def cadastro(request, template_name='usuarios/cadastro.html'):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        conf_senha = request.POST['password2']

        if campo_vazio(nome):
            messages.error(request, 'O campo nome não pode ficar em branco')
            return redirect('usuarios:cadastro')

        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco')
            return redirect('usuarios:cadastro')

        if senhas_nao_sao_iguais(senha, conf_senha):
            messages.error(request, 'As senhas não são iguais')
            return redirect('usuarios:cadastro')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('usuarios:cadastro')

        if User.objects.filter(username=nome).exists():
            messages.error(request,'Usuário já cadastrado')
            return redirect('usuarios:cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('usuarios:login')
    else:
        return render(request, template_name)


def criar_receita(request, template_name='usuarios/criar_receita.html'):
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