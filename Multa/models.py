from django.db import models

# Create your models here.

'''class Multa(models.Model):
    socio = models.ForeignKey('Socio', on_delete=models.CASCADE)
    prestamo = models.ForeignKey('Prestamo', on_delete=models.CASCADE)
    costo_adicional = models.DecimalField(max_digits=10, decimal_places=2)
    observacion = models.CharField(max_length=100)

    def __str__(self):
        return f"Multa {self.id} - Socio {self.socio_id} - Prestamo {self.prestamo_id}"
        '''
class Multa(models.Model):
    socio_id = models.IntegerField()
    prestamo_id = models.IntegerField()
    costo_adicional = models.DecimalField(max_digits=10, decimal_places=2)
    observacion = models.CharField(max_length=100)
