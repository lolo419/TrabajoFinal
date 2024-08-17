from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import login, logout, authenticate

from django.template import Template, Context, loader
from django import forms
from applogin import forms

def registroTemp(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, f"C:/Users/Lolo/Desktop/PROYECTO FINAL/plantillas/pagPrincipal.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, f"C:/Users/Lolo/Desktop/PROYECTO FINAL/plantillas/pagPrincipal.html", {"mensaje":"Datos incorrectos"})
           
        else:

            return render(request, "pagPrincipal.html", {"mensaje":"Formulario erroneo"})

    form = AuthenticationForm()

    return render(request, f"C:/Users/Lolo/Desktop/PROYECTO FINAL/plantillas/login.html", {"form": form})

def subidaDedts(request):
    
    if request.method == 'POST':
        
        cuerpo = Notas.Cuerpo ( request.POST[''])
        
        cuerpo.save()
        
        return render(request,"appregistro/pagPrincipal.html")

    return render(request, "applogin/subidaDeDatos.html")



