from django.db import models


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    descripcion = models.TextField()
    disponibilidad = models.BooleanField(default=True)
    codigo = models.CharField(max_length=50, unique=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return f"[{self.codigo}] {self.titulo} - {self.autor}"
