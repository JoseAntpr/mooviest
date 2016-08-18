# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth import logout as django_logout,authenticate, login as django_login
from django.contrib.auth.models import User
from .models import Profile
from users.forms import LoginForm,RegisterForm

# Create your views here.
def login(request):
    error_messages = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            if '@' in username:
                user_aux = User.objects.filter(email=username)[0]
                user = authenticate(username=user_aux.username,password=password)
            else:
                user = authenticate(username=username, password=password)

            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos')
            else:
                if user.is_active:
                    django_login(request,user)
                    return redirect('home')
                else:
                    error_messages.append("El usuario no está activo")
    else:
        form = LoginForm()
    context={
        'errors': error_messages,
        'login_form': form
    }
    return render(request, 'users/login.html',context)

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')

            user_model = User.objects.create_user(username=username,password=password,email=email)
            #Aunque no guarde nada del profile, pero asi queda la referencia creada
            user_profile = Profile()
            user_profile.user = user_model
            # Guardamos el perfil
            user_profile.save()
            #redirigimos
            user = authenticate(username=username, password=password)
            django_login(request,user)
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
        'register_form': form
    }
    return render(request,'users/register.html',context)
