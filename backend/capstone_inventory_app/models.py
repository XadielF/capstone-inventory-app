# structura para la base de datos
from django.db import models

class Propiedad(models.Model):
    tablilla = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    num_serie = models.CharField(max_length=50) # Numero de serie
    cantidad = models.CharField(max_length=10)
    condicion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=50)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    Propiedad_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.tablilla
    
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    llave_usuario = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)
    Usuario_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.nombre