from django.db import models

# Create your models here.
class Vinilo(models.Model):
    banda = models.CharField(max_length=30)
    nombreDisco = models.CharField(max_length=30)
    precio = models.IntegerField()
    indNacional = models.BooleanField()

class cd(models.Model):
    banda = models.CharField(max_length=30)
    nombreDisco = models.CharField(max_length=30)
    precio = models.IntegerField()
    indNacional = models.BooleanField()

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    telefono = models.IntegerField()

