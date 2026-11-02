from django.db import models

class AdminAuditoria(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100)
    accion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.id} - {self.usuario} - {self.accion} - {self.fecha}"