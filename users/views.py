# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.contrib.auth import logout as django_logout,authenticate, login as django_login, update_session_auth_hash
from django.contrib.auth.models import User
from movie.models import Country,Lang
from .models import Profile,RELATIONSHIP_FOLLOWING
from users.forms import LoginForm,RegisterForm,SettingForm,PasswordForm
from django.shortcuts import get_object_or_404

# Create your views here.
def login(request):
    error_messages = []
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            if '@' in username:
                try:
                    username = User.objects.get(email=username)
                except User.DoesNotExist:
                    username = None

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
            born = cleaned_data.get('born')
            password = cleaned_data.get('password')
            email = cleaned_data.get('email')

            user_model = User.objects.create_user(username=username,password=password,email=email)
            #Aunque no guarde nada del profile, pero asi queda la referencia creada
            user_profile = Profile()
            user_profile.user = user_model
            user_profile.lang = Lang.objects.get(code="es")
            # Guardamos el perfil
            user_profile.save()
            #redirigimos
            user = authenticate(username=username, password=password)
            django_login(request,user)
            return redirect('home')
    else:
        form = RegisterForm()
    context = {
        'register_form': form,
    }
    return render(request,'users/register.html',context)

def settingInfo(request):
    if request.method == 'POST':
        form = SettingForm(request.user,request.POST,request.FILES)
        if form.is_valid():
            if form.cleaned_data['avatar'] is None:
                request.user.profile.avatar = request.user.profile.avatar
            else:
                request.user.profile.avatar = form.cleaned_data['avatar']

            request.user.username = form.cleaned_data.get('username')
            request.user.first_name = form.cleaned_data.get('firstname')
            request.user.last_name = form.cleaned_data.get('lastname')
            request.user.email = form.cleaned_data.get('email')
            request.user.profile.born = form.cleaned_data.get('born')
            request.user.profile.gender = form.cleaned_data.get('gender')
            request.user.profile.country = form.cleaned_data.get('country')
            request.user.profile.city = form.cleaned_data.get('city')
            request.user.profile.postalCode = form.cleaned_data.get('postalcode')

            request.user.save()
            request.user.profile.save()

            return redirect('home')

    else:
        form = SettingForm(request.user,
            initial={
                    'username':request.user.username,
                    'firstname':request.user.first_name,
                    'lastname':request.user.last_name,
                    'email':request.user.email,
                    'born':request.user.profile.born,
                    'gender':request.user.profile.gender,
                    'country':request.user.profile.country,
                    'city': request.user.profile.city,
                    'postalcode' : request.user.profile.postalCode,
                }
        )
    context = {
        'setting_form': form
    }
    return render(request,'users/setting.html',context)
def settingPassword(request):
    if request.method == 'POST':
        form = PasswordForm(request.user,request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            new_password = form.cleaned_data.get('new_password')
            new_password2 = form.cleaned_data.get('new_password2')

            request.user.set_password(new_password)
            request.user.save()

            update_session_auth_hash(request,request.user)

            return redirect('home')
    else:
        form = PasswordForm(request.user)
    context = {
        'password_form': form
    }
    return render(request,'users/password.html',context)

def profile(request,user_id):
    userProfile = User.objects.get(pk=user_id)
    followers = userProfile.profile.get_followers()
    followings = userProfile.profile.get_following()
    seenlist = userProfile.profile.get_seenlist()
    watchlist = userProfile.profile.get_watchlist()
    favouritelist = userProfile.profile.get_favouritelist()
    likeCelebritiesList = userProfile.profile.get_likecelebrities()
    context = {
        'userProfile':userProfile,
        'followings': followings,
        'followers': followers,
        'seenlist': seenlist,
        'watchlist':watchlist,
        'favouritelist':favouritelist,
        'likeCelebritiesList': likeCelebritiesList
    }
    return render(request,'users/profile.html',context)

def follow(request, user_id):
    print("Entra en esta funcion")
    userFollowed = User.objects.get(pk = user_id)
    user = request.user

    if request.method == "POST":
        if 'follow' in request.POST:
            user.profile.follow(userFollowed.profile,RELATIONSHIP_FOLLOWING)
        elif 'unfollow' in request.POST:
            user.profile.unfollow(userFollowed.profile,RELATIONSHIP_FOLLOWING)
    else:
        print("ERROR: not followed")

    return redirect('/profile/' + user_id)
