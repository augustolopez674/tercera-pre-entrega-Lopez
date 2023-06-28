from django.urls import path
from inicio import views

app_name = 'inicio' 

urlpatterns = [
    path('', views.inicio, name ='inicio'),
    path('clientes/crear/', views.crear_cliente, name ='crear_cliente'),
    path('productos/crear/', views.crear_producto, name ='crear_producto'),
]
