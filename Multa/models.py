from django.db import models
from socios.models import Socio
from prestamo.models import Prestamo


class Multa(models.Model):
    id = models.AutoField(primary_key=True)
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
    prestamo = models.ForeignKey(
        Prestamo,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    costo_adicional = models.DecimalField(max_digits=10, decimal_places=2)
    observacion = models.TextField()

    def __str__(self):
        socio_nombre = self.socio.nombre if self.socio else "Sin socio"
        libro_titulo = (
            self.prestamo.libro.titulo
            if self.prestamo and self.prestamo.libro
            else "Sin libro"
        )
        total = (
            self.prestamo.libro.costo + self.costo_adicional
            if self.prestamo and self.prestamo.libro
            else self.costo_adicional
        )
        return f"Multa de {socio_nombre} por '{libro_titulo}': ${total:.2f}"
