from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, get_user_model
from accounts.forms import CustomUserChangeForm, CustomPasswordChangeForm
from .forms import ProfileForm, CustomProfileForm, CustomPasswordChangeForm, CustomUserChangeForm
from .models import Profile

@login_required
def profile_view(request):
    if request.method == 'POST':
        if 'update_email' in request.POST:
            user_form = CustomUserChangeForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                return redirect('profile')  # Redirige a la página del perfil después de guardar
        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Mantiene la sesión del usuario activa después del cambio de contraseña
                return redirect('profile')  # Redirige a la página del perfil después de cambiar la contraseña
    else:
        user_form = CustomUserChangeForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)

    return render(request, 'profiles/profile.html', {
        'user_form': user_form,
        'password_form': password_form
    })
@login_required
def update_profile_view(request):
    if request.method == 'POST':
        user_form = CustomUserChangeForm(request.POST, instance=request.user)
        profile_form = CustomProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if 'update_profile' in request.POST:
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                return redirect('profile')

    else:
        user_form = CustomUserChangeForm(instance=request.user)
        profile_form = CustomProfileForm(instance=request.user.profile)
    
    return render(request, 'accounts/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
    
@login_required
def delete_profile_view(request):
    request.user.delete()
    return redirect('signup')

@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Actualiza la sesión para que el usuario siga autenticado
            return redirect('profile')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    
    return render(request, 'accounts/change_password.html', {'form': form})