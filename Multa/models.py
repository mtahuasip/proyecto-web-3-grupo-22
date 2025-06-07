from django.db import models
from socios.models import Socio
from prestamo.models import prestamo

class Multa(models.Model):
    multa_ID = models.AutoField(primary_key=True)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE,null=True,blank=True)
    prestamo = models.ForeignKey(prestamo, on_delete=models.CASCADE,null=True,blank=True)
    costo_adicional = models.DecimalField(max_digits=10, decimal_places=2)
    observacion = models.CharField(max_length=100)

    def __str__(self):
        return f"Multa #{self.multa_ID} - Socio: {self.socio.nombre}"