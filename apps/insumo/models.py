from django.db import models

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    fecha_ingreso = models.DateField()

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.cantidad} - {self.fecha_ingreso}"