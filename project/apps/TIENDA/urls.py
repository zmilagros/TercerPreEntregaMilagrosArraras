from django.urls import path, include
from .views import inicioTienda, categorias
from clientes.views import clientes
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from productos.views import ProductoList


urlpatterns = [
    path('', inicioTienda, name="inicioTienda"),
    path('about/', clientes, name='clientes'),
    path('products/', ProductoList.as_view(), name='productos'), 
    path('products/', include('productos.urls'), name='productos'),
    path('store/', categorias, name='categorias'),
]

urlpatterns += staticfiles_urlpatterns()