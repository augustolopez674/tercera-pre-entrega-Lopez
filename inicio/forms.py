from django import forms
from django.contrib.auth.models import User

class CrearClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=10)
    apellido = forms.CharField(max_length=10)
    edad = forms.IntegerField()
    email = forms.EmailField()
    fecha_nacimiento = forms.DateField(required=False)

class CrearProductoFormulario(forms.Form):
    categoria = forms.CharField(max_length=20)
    nombre = forms.CharField(max_length=20)
    precio = forms.IntegerField()
    descripcion = forms.CharField()
    imagen = forms.ImageField(required=False)
    fecha = forms.DateField(required=False)
    
    
    
class BuscarProductoFormulario(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    