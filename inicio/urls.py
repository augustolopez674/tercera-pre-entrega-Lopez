from django.urls import path
from inicio import views

app_name = 'inicio' 

urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('clientes/crear/', views.crear_cliente, name ='crear_cliente'),
    path('productos/crear/', views.crear_producto, name ='crear_producto'),
    path('productos/', views.listar_productos, name ='listar_productos'),
    path('productos/<int:pk>', views.DetalleProducto.as_view(), name ='detalle_producto'),
    path('productos/<int:pk>/modificar/', views.ModificarProducto.as_view(), name ='modificar_producto'),
    path('productos/<int:pk>/eliminar/', views.EliminarProducto.as_view(), name ='eliminar_producto'),
]
