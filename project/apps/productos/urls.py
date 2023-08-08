from django.urls import path
from .views import ProductoList, ProductoCreate, ProductoDetail, ProductoUpdate, ProductoDelete


app_name = 'productos'

urlpatterns = [
    path('', ProductoList.as_view(), name='productos'),  # Lista de productos
    path('crearproducto/', ProductoCreate.as_view(), name='crear_producto'),
    path('detalleproducto/<int:pk>/', ProductoDetail.as_view(), name='detalle_producto'),  # Detalles del producto
    path('editarproducto/<int:pk>', ProductoUpdate.as_view(), name='editar_producto'),  # Editar producto
    path('eliminarproducto/<int:pk>/', ProductoDelete.as_view(), name='eliminar_producto'), # Eliminar producto
]




