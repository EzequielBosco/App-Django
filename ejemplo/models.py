from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=10)
    fecha_de_nacimiento = models.DateField()

    def __str__(self):
        return f" ID:{self.id} Nombre:{self.nombre}, Apellido:{self.apellido}, Fecha Nacimiento:{self.fecha_de_nacimiento}"