from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm
from django.contrib import messages

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, "libro/lista_libros.html", {"libros": libros})

def detalle_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    return render(request, "libro/detalle_libro.html", {"libro": libro})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)  # request.FILES para manejar imagen
        if form.is_valid():
            form.save()
            messages.success(request, "Libro creado correctamente.")
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, "libro/formulario_libro.html", {'form': form, 'accion': 'Crear'})

def editar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado correctamente.")
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, "libro/formulario_libro.html", {'form': form, 'accion': 'Editar'})

def eliminar_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, "Libro eliminado.")
        return redirect('lista_libros')
    return render(request, "libro/confirmar_eliminacion.html", {'libro': libro})
