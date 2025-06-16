from django import forms
from .models import Socio

class SocioEditarForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['ci', 'direccion', 'celular']
