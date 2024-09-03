from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,  update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from profiles.models import Profile
from .forms import CustomUserChangeForm, CustomPasswordChangeForm


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')
def home_view(request):
    return render(request, 'home.html')

@login_required
def update_profile_view(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')  # Redirige a la página del perfil después de guardar
    else:
        user_form = CustomUserChangeForm(instance=request.user)

    return render(request, 'accounts/update_profile.html', {'user_form': user_form})

@login_required
def change_password_view(request):
    if request.method == 'POST':
        password_form = CustomPasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)  # Mantiene la sesión del usuario activa después del cambio de contraseña
            return redirect('profile')  # Redirige a la página del perfil después de cambiar la contraseña
    else:
        password_form = CustomPasswordChangeForm(request.user)

    return render(request, 'accounts/change_password.html', {'password_form': password_form})