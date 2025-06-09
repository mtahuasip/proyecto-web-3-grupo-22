from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'  # Incluye todos los campos del modelo Libro

        # Etiquetas personalizadas (opcional)
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'editorial': 'Editorial',
            'anio': 'Año',
            'imagen': 'Imagen del Libro',
            'categoria': 'Categoría',
            'disponible': '¿Disponible?',
        }

        # Widgets personalizados (opcional)
        widgets = {
            'anio': forms.NumberInput(attrs={'min': 0, 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

        # Textos de ayuda (opcional)
        help_texts = {
            'anio': 'Ingrese el año de publicación del libro.',
            'imagen': 'Suba una imagen de portada en formato JPG o PNG.',
        }
