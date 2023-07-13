from django.urls import path
from .views import *
from .views import clientes, productos, categorias
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', inicioTienda, name="inicioTienda"),
    path('about/', clientes, name='clientes'),
    path('products/', productos, name='productos'),
    path('store/', categorias, name='categorias'),
]

urlpatterns += staticfiles_urlpatterns()