from django import forms
from .models import Prestamo
from Libro.models import Libro
from socios.models import Socio

class PrestamoForm(forms.ModelForm):
    libro = forms.ModelChoiceField(
        queryset=Libro.objects.all(),
        label="Libro",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    socio = forms.ModelChoiceField(
        queryset=Socio.objects.all(),
        label="Socio",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    fecha_devolucion = forms.DateField(
        required=False,  
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label="Fecha de Devolución"
    )

    class Meta:
        model = Prestamo
        fields = ['libro', 'socio', 'fecha_limite']
        widgets = {'fecha_limite': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),}
        labels = {'fecha_limite': 'Fecha Límite de Devolución',}

    def clean_fecha_limite(self):
        fecha_limite = self.cleaned_data.get('fecha_limite')
        if fecha_limite is None:
            raise forms.ValidationError("Debes ingresar una fecha límite de devolución.")
        return fecha_limite

    def save(self, commit=True):
        prestamo = super().save(commit=False)
        prestamo.libro = self.cleaned_data['libro']
        prestamo.socio = self.cleaned_data['socio']
        prestamo.fecha_devolucion = self.cleaned_data.get('fecha_devolucion')
        if commit:
            prestamo.save()
        return prestamo
