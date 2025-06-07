from django.db import models

# Create your models here.
from django.db import models

class Libro(models.Model):
    libro_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    disponibilidad = models.BooleanField(default=True)
    codigo = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
