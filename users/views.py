from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render

from users.forms import LoginForm, SignupForm


def login(request):
    if request.user.is_authenticated:
        messages.error(request, 'Você já está logado. Para sair, selecione "Logout".')
        return redirect('index')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if not form.is_valid():
            messages.error(request, 'Campos inválidos!')
            return redirect('login')

        username = form['username'].value()
        password = form['password'].value()
        
        user = auth.authenticate(
            request,
            username=username,
            password=password,
        )
        if user:
            auth.login(request, user)
        else:
            messages.error(request, 'Usuário e/ou senha inválidos!')
            return redirect('login')

        messages.success(request, f'Olá, {username}!')
        return redirect('index')

    return render(request, 'users/login.html', {'form': LoginForm()})


def signup(request):
    form = SignupForm()

    if request.user.is_authenticated:
        messages.error(request, 'Você já está logado. Para sair, selecione "Logout".')
        return redirect('index')

    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            username = form['username'].value()
            email = form['email'].value()
            password = form['password'].value()

            if User.objects.filter(Q(username=username) | Q(email=email)).exists():
                messages.error(request, 'Username e/ou email já cadastrados!')
                return redirect('signup')

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            user.save()

            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')

    return render(request, 'users/signup.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Até a próxima!')
    
    return redirect('login')
