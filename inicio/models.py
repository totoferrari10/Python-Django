from django.db import models

# Create your models here.

# class Ropa(models.Model):
#     marca= models.CharField(max_length=20)
#     corte= models.CharField(max_length=20)
#     talle=  models.IntegerField()
    
#     def __str__(self):
#         return f"{self.marca} {self.talle}"

from django.db import models

class Coworking(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del espacio
    descripcion = models.TextField()  # Descripción del espacio
    capacidad = models.IntegerField()  # Capacidad del espacio en número de personas
    precio_por_hora = models.DecimalField(max_digits=6, decimal_places=2)  # Precio por hora
    disponibilidad = models.BooleanField(default=True)  # Si está disponible o no
    
    def __str__(self):
        return f"{self.nombre} - Capacidad: {self.capacidad} personas"