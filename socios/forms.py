from django import forms
from .models import Socio


class SocioForm(forms.ModelForm):
    pass


#     ci = forms.CharField(
#         max_length=10,
#         widget=forms.TextInput(attrs={
#             'pattern': '[0-9]+',
#             'maxlength': '10',
#             'class': 'form-control'
#         })
#     )

#     celular = forms.CharField(
#         max_length=8,
#         widget=forms.TextInput(attrs={
#             'pattern': '[0-9]+',
#             'maxlength': '8',
#             'class': 'form-control'
#         })
#     )

#     class Meta:
#         model = Socio
#         fields = ['nombre', 'ci', 'direccion', 'correo', 'contraseña', 'celular',]
#         widgets = {
#             'contraseña': forms.PasswordInput(attrs={'class': 'form-control'}),
#             'nombre': forms.TextInput(attrs={'class': 'form-control'}),
#             'direccion': forms.TextInput(attrs={'class': 'form-control'}),
#             'correo': forms.EmailInput(attrs={'class': 'form-control'}),
#         }
# def clean_ci(self):
#         ci = self.cleaned_data['ci']
#         if not ci.isdigit():
#             raise forms.ValidationError("El C.I. debe contener solo números.")
#         if len(ci) > 10:
#             raise forms.ValidationError("El C.I. no puede tener más de 10 dígitos.")
#         return ci
# def clean_celular(self):
#         celular = self.cleaned_data['celular']
#         if not celular.isdigit():
#             raise forms.ValidationError("El número de celular debe contener solo números.")
#         if len(celular) != 8:
#             raise forms.ValidationError("El número de celular debe tener exactamente 8 dígitos.")
#         return celular
