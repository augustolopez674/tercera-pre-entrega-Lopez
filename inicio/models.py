from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    edad = models.IntegerField()
    email = models.EmailField()
    fecha_nacimiento = models.DateField(null=True)
    
    
class Producto(models.Model):
    categoria = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()    
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Precio: {self.precio}'