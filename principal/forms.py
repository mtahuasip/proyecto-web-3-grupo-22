from django import forms
from socios.models import Socio


class SocioRegistroForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombres", max_length=100)
    last_name = forms.CharField(label="Apellidos", max_length=100)
    email = forms.EmailField()
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    ci = forms.CharField(label="Carnet de identidad")
    direccion = forms.CharField(
        label="Dirección",
        widget=forms.Textarea,
        required=False,
    )
    celular = forms.CharField()

    class Meta:
        model = Socio
        fields = [
            "ci",
            "direccion",
            "celular",
        ]


class SocioLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
