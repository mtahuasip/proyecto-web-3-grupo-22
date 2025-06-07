from django import forms
from .models import Multa

class MultaForm(forms.ModelForm):
    class Meta:
        model = Multa
        fields = ['socio', 'prestamo', 'costo_adicional', 'observacion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añadir clase 'form-control' a todos los campos
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
