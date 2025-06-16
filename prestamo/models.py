from django.db import models
from socios.models import Socio
from Libro.models import Libro


class Prestamo(models.Model):
    id = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, null=True, blank=True)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    fecha_pretamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    fecha_limite = models.DateField()
    # costo = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_costo(self):
        return self.libro.costo

    def __str__(self):
        libro_str = self.libro.titulo if self.libro else "Libro no asignado"
        socio_str = (
            self.socio.user.get_full_name() if self.socio else "Socio no asignado"
        )
        return f"Préstamo: '{libro_str}' a {socio_str} (Devolución: {self.fecha_devolucion})"
