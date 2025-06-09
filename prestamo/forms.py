from django import forms
from .models import Prestamo

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['libro', 'socio', 'fecha_devolucion', 'fecha_limite' ]
        widgets = {
            'libro': forms.Select(attrs={'class': 'form-control'}),
            'socio': forms.Select(attrs={'class': 'form-control'}),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_limite': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'libro': 'Libro',
            'socio': 'Socio',
            'fecha_devolucion': 'Fecha de Devolución',
            'fecha_limite': 'Fecha Límite',
        }
