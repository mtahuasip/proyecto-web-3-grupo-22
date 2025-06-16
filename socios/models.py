from django.db import models
from django.contrib.auth.models import User

class Socio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ci = models.CharField("Carnet de Identidad", max_length=20)
    direccion = models.TextField("Dirección", blank=True)
    celular = models.CharField("Celular", max_length=20)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

