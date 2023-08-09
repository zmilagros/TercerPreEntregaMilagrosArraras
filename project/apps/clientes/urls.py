from .views import clientes
from django.urls import path
from clientes.views import *
from django.contrib.auth.views import LogoutView

app_name = 'clientes'

urlpatterns = [
    path('', clientes, name='clientes'), 
    path("login/", iniciar_sesion, name="usuarios-login"),
    path("registrar/", registrar_usuario, name="usuarios-registrar"),
    path("editar/", editar_usuario, name="usuarios-editar"),
    path("logout/", LogoutView.as_view(template_name="usuarios/logout.html"), name="usuarios-logout"),
]