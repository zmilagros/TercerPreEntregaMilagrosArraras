# clientes app urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import iniciar_sesion, registrar_usuario, about, editar_usuario

app_name = 'clientes'

urlpatterns = [
    path('login/', iniciar_sesion, name='usuarios-login'),
    path('registrar/', registrar_usuario, name='usuarios-registrar'),
    path('about/', about, name='about'),
    path('editar/', editar_usuario, name='usuarios-editar'),
    path('logout/', LogoutView.as_view(template_name='clientes/logout.html'), name='usuarios-logout'),
]