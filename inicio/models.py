from django.db import models

class OrdenCompras(models.Model):
    norden = models.CharField(max_length=100)
class Estado(models.Model):
    nombre = models.CharField(max_length=100)

class Dispositivo(models.Model):
    nserie = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    fcreacion = models.DateField(auto_now_add=True)
    fingreso = models.DateTimeField()
    tipo_dispositivo = models.CharField(max_length=100)
    norden = models.ForeignKey(OrdenCompras, on_delete=models.CASCADE)
    estado_id = models.ForeignKey(Estado, on_delete=models.CASCADE)
    observacion =models.models.TextField()
    

class Gerencia(models.Model):
    nombre = models.CharField(max_length=100)
        
# class Departamento(models.Model):
    # opcgerencia = [
    #     ("GAF" , "Gerencia de Administración y Finanzas"),
    #     ("GPMO" , "Gerencia de PMO"),
    #     ("GLLTT" , "Gerencia Ingeniería y Construcción LLTT"),
    #     ("GMA" , "Gerencia Medio Ambiente y Comunidades"),
    #     ("GEECC" , "Gerencia Ingeniería y Construcción EECC"),
    #     ("GG" , "Gerencia General")
    #]
    # nombre = models.CharField(max_length=100, choices=opcgerencia, default="GAF")
    # ccosto = models.CharField(max_length=100)

class Software(models.Model):
    nombre = models.CharField(max_length=100)
    version = models.CharField(max_length=50)
    fcompra = models.DateTimeField()
    cantidad = models.IntegerField(default=0)
    duracion = models.IntegerField(default=1)
    factualiza = models.DateTimeField()
    norden = models.ForeignKey(OrdenCompras, on_delete=models.CASCADE)
    valor = models.IntegerField(null=True)
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gerencia = models.ForeignKey(Gerencia, on_delete=models.CASCADE)
    
    
    
    
    
    
    
    