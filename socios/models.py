from django.db import models

class Socio(models.Model):
    nombre = models.CharField(max_length=50)
    ci = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nombre
