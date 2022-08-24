from django.db import models

# Create your models here.
class Vinilo(models.Model):
    banda = models.CharField(max_length=30)
    nombreDisco = models.CharField(max_length=30)
    precio = models.IntegerField()
    

    def __str__(self):
        return f"Banda: {self.banda} - Disco: {self.nombreDisco} - Precio: {self.precio}"

class cd(models.Model):
    banda = models.CharField(max_length=30)
    nombreDisco = models.CharField(max_length=30)
    precio = models.IntegerField()
    

    def __str__(self):
        return f"Banda: {self.banda} - Disco: {self.nombreDisco} - Precio: {self.precio}"

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Telefono: {self.telefono}"

