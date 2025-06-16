from django.db import models
from django.contrib.auth.models import User


class Socio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    ci = models.CharField(max_length=20)
    direccion = models.TextField(blank=True)
    celular = models.CharField(max_length=20)

    def __str__(self):
        return self.user.get_full_name()
