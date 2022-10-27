from django.db import models
from django.utils import timezone
# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    empresa = models.CharField(max_length=20, blank=False, null=False)
    valor = models.CharField(max_length=20, blank=False, null=False)



class productor(models.Model):
    productos = models.CharField(max_length=20, blank=False, null=False)
    precio = models.CharField(max_length=20, blank=False, null=False)
    cantidad = models.IntegerField()
    calidad = models.CharField(max_length=20, blank=False, null=False)


Estado = (('disponible','Disponible'),('terminado','Terminado'),('proceso','Proceso'),('venta','Venta'))

class Productos(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fotografia = models.CharField(max_length=200, blank=False, null=False)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=10, choices=Estado)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.estado

class ProductosVenta(models.Model):
    nombre = models.CharField(max_length = 75)
    solicitud = models.CharField(max_length = 200)
    cierre_oferta = models.DateField()
    comuna = models.CharField(max_length = 30)

class Transporte(models.Model):
    nombre = models.CharField(max_length = 75)
    t_transporte = models.CharField(max_length = 75)
    comuna = models.CharField(max_length = 75)
    