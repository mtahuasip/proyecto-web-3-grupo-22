from django.shortcuts import render, get_object_or_404
from Libro.models import Libro


def inicio(request):
    return render(request, "principal/inicio.html")


def catalogo(request):
    libros = Libro.objects.all()
    return render(request, "principal/catalogo.html", {"libros": libros})


def catalogo_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, "principal/catalogo_libro.html", {"libro": libro})
