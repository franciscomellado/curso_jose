from django.db import models

# Create your models here.
# comentario
class Estado(models.Model):
    nombre = models.CharField(max_length=100)

class Dispositivo(models.Model):
    nserie = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    fcreacion = models.DateField(auto_now_add=True)
    fingreso = models.DateTimeField()
    tipo_dispositivo = models.CharField(max_length=100)
    norden = models.CharField(max_length=100)
    estado_id = models.ForeignKey(Estado, on_delete=models.CASCADE)
    observacion =models.models.TextField()
    
class Departamento(models.Model):
    opcgerencia = [
        ("GAF" , "Gerencia de Administración y Finanzas"),
        ("GPMO" , "Gerencia de PMO"),
        ("GLLTT" , "Gerencia Ingeniería y Construcción LLTT"),
        ("GMA" , "Gerencia Medio Ambiente y Comunidades"),
        ("GEECC" , "Gerencia Ingeniería y Construcción EECC"),
        ("GG" , "Gerencia General")
    ]
    nombre = models.CharField(max_length=100, choices=opcgerencia, default="GAF")
    
    
    
    
    
    
    