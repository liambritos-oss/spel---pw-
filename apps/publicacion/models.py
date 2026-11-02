from django.db import models

class Publicacion(models.Model): 
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    nivel_educativo = models.CharField(max_length=30, choices=[
        ('Primaria', 'primaria'),
        ('Secundaria', 'secundaria'),
        ('Universidad', 'universidad'),  
    ])

    infraestructura = models.CharField(max_length=30, choices=[
        
        ('Aula', 'aula'),
        ('Aula de talleres', 'aula de talleres'), 
        ('Baño', 'baño'),
        ('Biblioteca', 'biblioteca'),
        ('Comedor', 'comedor'),
        ('Direccion', 'direccion'),
        ('Gabinete de orientación', 'gabinete de orientación'),
        ('Gimnasio', 'gimnasio'),
        ('Laboratorio', 'laboratorio'),  
        ('Patio', 'patio'),
        ('Porteria', 'porteria'),
        ('Pañol', 'pañol'),
        ('Preseptoria', 'preseptoria'),
        ('Secretaria', 'secretaria'),
        ('Sala de profesores', 'sala de profesores'),
        ('Sala de informática', 'sala de informática'),
        ('Sala de teatro', 'sala de teatro'),
        ('Sala de calderas', 'sala de calderas'),
    ])

    def __str__(self):
        return f"{self.titulo} - {self.contenido} - {self.fecha_publicacion} - {self.nivel_educativo} - {self.infraestructura}"