from django.db import models

class prestamo (models.Model):
    libro_id= models.IntegerField()
    socio_id = models.IntegerField()
    prestamo_id= models.AutoField(primary_key=True)
    fecha_pretamo=models.DateField(auto_now_add=True)
    fecha_devolucion= models.DateField()
    fecha_limite=models.DateField()
    costo= models.DecimalField( max_digits=10, decimal_places=2)
    

    class Meta:
        db_table='prestamo'

    def __str__(self):
        return f"prestamo #{self.prestamo_id} - libro {self.libro_id} a socio {self.socio_id}"


