from django.utils import timezone
from django import forms
from socios.models import Socio


class SocioRegistroForm(forms.ModelForm):
    first_name = forms.CharField(
        label="Nombres",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control w-100"}),
    )
    last_name = forms.CharField(
        label="Apellidos",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control w-100"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control w-100"})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control w-100"}),
    )
    ci = forms.CharField(
        label="Carnet de identidad",
        widget=forms.TextInput(attrs={"class": "form-control w-100"}),
    )
    direccion = forms.CharField(
        label="Dirección",
        widget=forms.Textarea(attrs={"class": "form-control w-100", "rows": 3}),
        required=False,
    )
    celular = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control w-100"})
    )

    class Meta:
        model = Socio
        fields = [
            "first_name",
            "last_name",
            "email",
            "password",
            "ci",
            "direccion",
            "celular",
        ]


class SocioLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control w-100"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control w-100"})
    )


class AdminLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control w-100"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control w-100"})
    )


class FechaDevolucionForm(forms.Form):
    fecha_devolucion = forms.DateField(
        label="Fecha de devolución",
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "min": timezone.now().date().isoformat(),
                "class": "form-control w-100",
            }
        ),
    )

    def clean_fecha_devolucion(self):
        fecha = self.cleaned_data["fecha_devolucion"]
        if fecha < timezone.now().date():
            raise forms.ValidationError(
                "La fecha de devolución no puede ser mayor a hoy."
            )
        return fecha
