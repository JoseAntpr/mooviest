# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    usr = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario',"class":"form-control",}))
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class RegisterForm(forms.Form):

    username = forms.CharField(min_length=4)
    email = forms.EmailField()
    password = forms.CharField(min_length=5,widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean_username(self):
        #Comprueba que no exista un username igual en la db
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('Nombre de usuario ya registrado.')
        return username
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
