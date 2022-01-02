from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def dashboard(request, template_name='usuarios/dashboard.html'):
    return render(request, template_name)


def login(request, template_name='usuarios/login.html'):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']

        if email == '' or senha == '':
            print('Os campos email e senha não podem ficar em branco')
            return redirect('usuarios:login')

        print(email, senha)

        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('usuarios:dashboard')
    else:
        return render(request, template_name)


def logout(request):
    pass


def cadastro(request, template_name='usuarios/cadastro.html'):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        conf_senha = request.POST['password2']

        if not nome.strip():
            print('O campo nome não pode ficar em branco')
            return redirect('cadastro')

        if not email.strip():
            print('O campo email não pode ficar em branco')
            return redirect('cadastro')

        if senha != conf_senha:
            print('As senhas não são iguais')
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect('cadastro')

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        print('Usuário cadastrado com sucesso')
        return redirect('usuarios:login')
    else:
        return render(request, template_name)
