from django.db import models
from django.contrib.auth.models import User



class Coworking(models.Model):
    nombre = models.CharField(max_length=100)  
    descripcion = models.TextField()  
    ambientes = models.IntegerField(default=0)
    capacidad = models.IntegerField()  
    precio_por_hora = models.DecimalField(max_digits=6, decimal_places=2)  
    disponibilidad = models.BooleanField(default=True)  
    mensaje = models.TextField() 
    
    def __str__(self):
        return f"{self.nombre} - Capacidad: {self.capacidad} personas"


opciones_consultas = [
    [0, "consulta"],
    [1, "reclamo"],
    [2, "sugerencias"],
    [3, "felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)  
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas) 
    mensaje= models.TextField()
    avisos= models.BooleanField()
    
    def __str__(self):
        return self.nombre
    
