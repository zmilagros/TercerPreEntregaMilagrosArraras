from django.urls import path, include
from .views import inicioTienda, categorias
from clientes.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from productos.views import ProductoList
from clientes.views import iniciar_sesion  

urlpatterns = [
    path('', inicioTienda, name="inicioTienda"),
    path('clientes/', iniciar_sesion, name='clientes'), 
    path('products/', ProductoList.as_view(), name='productos'), 
    path('products/', include('productos.urls'), name='productos'),
    path('store/', categorias, name='categorias'),
]
