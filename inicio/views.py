from django.shortcuts import render, redirect
from inicio.forms import CrearClienteFormulario, CrearProductoFormulario, BuscarProductoFormulario
from inicio.models import Cliente, Producto
# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_cliente(request):
    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearClienteFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            cliente = Cliente(nombre=info['nombre'],apellido=info['apellido'],edad=info['edad'],email=info['email'],fecha_nacimiento=info['fecha_nacimiento'])
            cliente.save()
            mensaje = f'Se creó el cliente {cliente.nombre} {cliente.apellido}'
        else:
            return render(request, 'inicio/crear_cliente.html', {'formulario': formulario})     
    
    formulario = CrearClienteFormulario()
    return render(request, 'inicio/crear_cliente.html', {'formulario': formulario, 'mensaje': mensaje})

def crear_producto(request):
    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearProductoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            producto = Producto(categoria=info['categoria'],nombre=info['nombre'],precio=info['precio'])
            producto.save()
            mensaje = f'Se creó el producto {producto.nombre}, de la categoria {producto.categoria} y precio {producto.precio}'
            return redirect('inicio:listar_productos')
        else:
            return render(request, 'inicio/crear_producto.html', {'formulario': formulario})     
    
    formulario = CrearProductoFormulario()
    return render(request, 'inicio/crear_producto.html', {'formulario': formulario, 'mensaje': mensaje})



def listar_productos(request):
    
    formulario = BuscarProductoFormulario(request.GET)
    if formulario.is_valid():
        nombre_producto = formulario.cleaned_data['nombre']
        listado_de_productos = Producto.objects.filter(nombre__icontains=nombre_producto)
        
    formulario = BuscarProductoFormulario()    
    return render(request, 'inicio/listar_productos.html', {'formulario': formulario, 'productos': listado_de_productos})