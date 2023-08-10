from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm
from clientes.forms import UserRegisterForm, UserEditForm
from clientes.models import *
from django.contrib.auth.decorators import login_required
from productos import *

# importo el paquete os para manejar nombres de archivo
import os

from django.shortcuts import render
from django.contrib.auth.decorators import login_required



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
            return redirect("productos: lista_productos")
        else:
            return render(request, "clientes/registrar_usuario.html", {"form": formulario, "errors": errors})

    formulario = UserRegisterForm()
    return render(request, "clientes/registrar_usuario.html", {"form": formulario, "errors": errors})


@login_required
def about(request):
    usuarios = usuarios.objects.all() 
    context = {"usuarios": usuarios}
    return render(request, "clientes/about.html", context)


@login_required
def editar_usuario(request):
    usuario = request.user
    if request.method == "POST":
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.save()

            return redirect("productos-inicio")
    else:
        formulario = UserEditForm(initial={"first_name": usuario.first_name, "last_name": usuario.last_name, "email": usuario.email})

    return render(request, "clientes/editar_usuario.html", {"form": formulario, "usuario": usuario})


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

