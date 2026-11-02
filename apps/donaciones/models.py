from django.db import models

class Donaciones(models.Model):
    colegio_destinado = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    producto = models.CharField(max_length=100)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.colegio_destinado} - {self.cantidad} - {self.producto} - {self.fecha}"