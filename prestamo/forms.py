from django import forms
from .models import Prestamo
from Libro.models import Libro
from socios.models import Socio

class PrestamoForm(forms.ModelForm):
    libro_id = forms.IntegerField(
        label="ID del Libro", 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    socio_id = forms.IntegerField(
        label="ID del Socio", 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Prestamo
        fields = ['libro_id', 'socio_id', 'fecha_limite']
        widgets = {
            'fecha_limite': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'fecha_limite': 'Fecha Límite de Devolución',
        }
    
    def clean_libro_id(self):
        libro_id = self.cleaned_data.get('libro_id')
        try:
            libro = Libro.objects.get(pk=libro_id)
        except Libro.DoesNotExist:
            raise forms.ValidationError("No existe un libro con ese ID.")
        return libro  

    def clean_socio_id(self):
        socio_id = self.cleaned_data.get('socio_id')
        try:
            socio = Socio.objects.get(pk=socio_id)
        except Socio.DoesNotExist:
            raise forms.ValidationError("No existe un socio con ese ID.")
        return socio

    def save(self, commit=True):
        prestamo = super().save(commit=False)
        prestamo.libro = self.cleaned_data['libro_id']
        prestamo.socio = self.cleaned_data['socio_id']
        if commit:
            prestamo.save()
        return prestamo