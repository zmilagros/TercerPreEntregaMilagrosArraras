from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',inicioTienda,name="inicioTienda"),
    path('clientes/',clientes,name="clientes"),
    path('productos/',productos,name="productos"),
    path('categorias/', views.categorias, name='categorias'),
]