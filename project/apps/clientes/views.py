from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from clientes.forms import UserRegisterForm, UserEditForm
from clientes.models import *
from django.contrib.auth.decorators import login_required
from productos import *
from django.http import HttpResponseServerError
from django.contrib import messages
from django.urls import reverse_lazy
# importo el paquete os para manejar nombres de archivo
import os

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def iniciar_sesion(request):
    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            user = authenticate(username=data["username"], password=data["password"])

            if user is not None:
                login(request, user)
                return redirect("productos:lista_productos")  # Redirigir a la página de inicio de la TIENDA
            else:
                return render(request, "clientes/login.html", {"form": formulario, "errors": "Credenciales no válidas"})
        else:
            return render(request, "clientes/login.html", {"form": formulario, "errors": formulario.errors})

    formulario = AuthenticationForm()
    return render(request, "clientes/login.html", {"form": formulario, "errors": errors})

def registrar_usuario(request):
    errors = ""
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            formulario.save()
            user = authenticate(username=data["username"], password=data["password1"])
            login(request, user)
            return redirect("productos:lista_productos")
        else:
            return render(request, "clientes/registrar_usuario.html", {"form": formulario, "errors": errors})

    formulario = UserRegisterForm()
    return render(request, "clientes/registrar_usuario.html", {"form": formulario, "errors": errors})


@login_required
def about(request):
    usuarios = usuarios.objects.all() 
    context = {"usuarios": usuarios}
    return render(request, "clientes/about.html", context)



@login_required(login_url=reverse_lazy('clientes:usuarios-login')) 
def editar_usuario(request):
    usuario = request.user
    if request.method == "POST":
        formulario = UserEditForm(request.POST, instance=usuario)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            if data["password1"]:  # Verifica si se proporcionó una nueva contraseña
                usuario.set_password(data["password1"])
            usuario.save()
            messages.success(request, 'Cambios guardados exitosamente.')
            return redirect("clientes:usuarios-login")
        else:
            messages.error(request, 'Error al guardar los cambios. Por favor, corrige los errores.')

    else:
        formulario = UserEditForm(instance=usuario)

    return render(request, "clientes/editar_usuario.html", {"form": formulario, "usuario": usuario})




@method_decorator(login_required(login_url=reverse_lazy('clientes:usuarios-login')), name='dispatch')
class AvatarUploadView(View):
    template_name = 'clientes/avatar_upload.html'

    def get(self, request):
        user = request.user
        avatar, created = Avatar.objects.get_or_create(user=user)
        return render(request, self.template_name, {'avatar': avatar})
    
    def post(self, request):
        user = request.user
        avatar, created = Avatar.objects.get_or_create(user=user)

        try:
            if 'imagen' in request.FILES:
                avatar.imagen = request.FILES['imagen']
                avatar.save()
                messages.success(request, 'Avatar cargado exitosamente.')
                return redirect('cargar_avatar')
        except Exception as e:
            messages.error(request, f'Error al cargar el avatar: {str(e)}')

        return render(request, self.template_name, {'avatar': avatar})


def avatar_usuario(usuario_activo):
    if usuario_activo.is_authenticated:
        if Avatar.objects.filter(user=usuario_activo.id).exists():
            imagen_model = Avatar.objects.get(user=usuario_activo.id)
            imagen_url = imagen_model.imagen.url
        else:
            imagen_url = ""
    else:
        imagen_url = ""
    return imagen_url

@login_required(login_url=reverse_lazy('clientes:usuarios-login'))
def mostrar_navbar(request):
    usuario_activo = request.user
    avatar_url = avatar_usuario(usuario_activo)

    context = {
        'avatar_url': avatar_url
    }
    return render(request, 'clientes/navbar.html', context)
