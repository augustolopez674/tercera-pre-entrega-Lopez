from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as app_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from usuarios.forms import FormularioCreacionUsuarios, FormularioEditarDatos
from django.urls import reverse_lazy
from usuarios.models import InfoExtra

# Create your views here.


def login(request):
    
    if request.method =='POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            user = authenticate(username=usuario, password=contrasenia)
            
            app_login(request, user)
            
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('inicio:inicio')
        else:
            return render(request, 'usuarios/login.html', {'formulario': formulario})    
    
    formulario = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'formulario': formulario})


def registrarse(request):
    
    if request.method == 'POST':
        formulario = FormularioCreacionUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
        else:
            return render(request, 'usuarios/registro.html', {'formulario': formulario})    
    
    formulario = FormularioCreacionUsuarios()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})


@login_required
def editar_perfil(request):
    
    
    info_extra_user = request.user.infoextra
    
    if request.method == 'POST':
        formulario = FormularioEditarDatos(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            avatar = formulario.cleaned_data.get('avatar')
            if avatar:
                info_extra_user.avatar = avatar
                info_extra_user.save()
            formulario.save()
            return redirect('inicio:inicio')
    else:
            formulario = FormularioEditarDatos(initial={'avatar': request.user.infoextra.avatar}, instance=request.user)    
    
    return render(request, 'usuarios/edicion_perfil.html', {'formulario': formulario})


class ModificarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/modificar_password.html'
    success_url = reverse_lazy('usuarios:editar_perfil')
