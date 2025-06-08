from django.db import models


class Socio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ci = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=50)
    celular = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} (CI: {self.ci}, Email: {self.correo})"
