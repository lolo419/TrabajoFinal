from django import forms
from django.shortcuts import render


from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from applogin import views
from applogin.views import *
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class UserRegisterForm(UserCreationForm):
    email = models.EmailField()
    password1 = models.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = models.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


def login_request(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"paginaPrincipal.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,f"C:/Users/Lolo/Desktop/PROYECTO FINAL/plantillas/registro.html" ,  {"form":form})

