# -*- coding: utf-8 -*-
from django import forms
from .models import GENDER_CHOICES
from movie.models import Country
from .models import Profile
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
import datetime

class LoginForm(forms.Form):

    usr = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario',"class":"form-control",}))
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class RegisterForm(forms.Form):

    username = forms.CharField(min_length=4)
    email = forms.EmailField()
    born = forms.DateField(widget = SelectDateWidget(years=range(1940,int(datetime.datetime.now().year))),required=False)
    password = forms.CharField(min_length=5,widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        #Comprueba que no exista un username igual en la db
        username = self.cleaned_data['username']
        if User.objects.filter(username=username.lower()):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username.lower()
    def clean_email(self):
        #Comprueba que no exista ningún email igual en la db
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un email igual en la db')
        return email
    def clean_password2(self):
        #Comprueba que password y password2 sean iguales
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2


class SettingForm(forms.Form):
    avatar = forms.ImageField(required=False)
    username = forms.CharField(min_length=4)
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)
    email = forms.EmailField()
    born = forms.DateField(widget = SelectDateWidget(years=range(1940,int(datetime.datetime.now().year))),required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect(),required=False)
    country = forms.ModelChoiceField(queryset=Country.objects.all(),required=False)
    city = forms.CharField(required=False)
    postalcode = forms.CharField(required=False)

    def __init__(self,user,*args,**kwargs):
        self.user = user
        super(SettingForm,self).__init__(*args,**kwargs)

    def clean_username(self):

        #Comprueba que no exista un username igual en la db
        username = self.cleaned_data['username']
        if not self.user.username == username and User.objects.filter(username=username.lower()) :
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        else:
            return username.lower()
    def clean_email(self):
        #Comprueba que no exista ningún email igual en la db
        email = self.cleaned_data['email']
        if not self.user.email == email:
            raise forms.ValidationError('Ya existe un email igual en la db')
        return email

class PasswordForm(forms.Form):
    password = forms.CharField(min_length=5,widget=forms.PasswordInput())
    new_password = forms.CharField(min_length=5,widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())

    def __init__(self,user,*args,**kwargs):
        self.user = user
        super(PasswordForm,self).__init__(*args,**kwargs)

    def clean_password(self):
        password = self.cleaned_data['password']
        if not self.user.check_password(password):
            raise forms.ValidationError('Contraseña incorrecta')
        return password

    def clean_password2(self):
        #Comprueba que password y password2 sean iguales
        new_password = self.cleaned_data['new_password']
        new_password2 = self.cleaned_data['new_password2']

        if password != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return password2
        #if not user.check_password(password):
        #    raise forms.ValidationError('Esta contraseña no es correcta')
        #return password
