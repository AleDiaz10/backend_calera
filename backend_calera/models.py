from django.db import models
from django.utils import timezone

class restaurante(models.Model):
    nombre = models.CharField(max_lenght=200)
    direccion = models.TextField()
    tel = models.TextField()
    horario = models.TextField()

    def save(self):
        self.save()

class plato(models.Model):
    nombre = models.CharField(max_lenght=200)
    precio = models.FloatField()

    def save(self):
        self.save()

class ingrediente(models.Model):
    nombre = models.CharField(max_lenght=200)
    precio = models.FloatField()

    def save(self):
        self.save()

class supermercado(models.Model):
    nombre = models.CharField(max_lenght=200)
    direccion = models.TextField()
    tel = models.TextField()
    horario = models.TextField()

    def save(self):
        self.save()

class producto(models.Model):
    nombre = models.CharField(max_lenght=200)
    precio = models.FloatField()

    def save(self):
        self.save()


class pedido(models.Model):
    nombre = models.CharField(max_lenght=200)
    #hora_solicitud= models.DateTimeField(blank=True, null=True)
    direccion = models.TextField()
    tel = models.TextField()
    pago = models.FloatField()
    total = models.FloatField()

    def save(self):
        self.save()