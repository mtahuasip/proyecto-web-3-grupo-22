from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro

# from .forms import MultaForm
from django.contrib import messages


def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, "libro/lista_libros.html", {"libros": libros})


def detalle_libro(request, id):
    libro = get_object_or_404(Libro, pk=id)
    return render(request, "libro/detalle_multa.html", {"libro": libro})


def crear_libro(request):
    pass
    # if request.method == 'POST':
    #     form = MultaForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Multa creada correctamente.")
    #         return redirect('lista_libros')
    # else:
    #     form = MultaForm()
    # return render(request, 'libro/formulario_multa.html', {'form': form, 'accion': 'Crear'})
    return render(request, "libro/formulario_libro.html")


def editar_libro(request, id):
    # multa = get_object_or_404(Multa, pk=id)
    # if request.method == 'POST':
    #     form = MultaForm(request.POST, instance=multa)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Multa actualizada correctamente.")
    #         return redirect('lista_libros')
    # else:
    #     form = MultaForm(instance=multa)
    # return render(request, 'libro/formulario_multa.html', {'form': form, 'accion': 'Editar'})
    return render(request, "libro/formulario_libro.html")


def eliminar_libro(request, id):
    # multa = get_object_or_404(Multa, pk=id)
    # if request.method == 'POST':
    #     multa.delete()
    #     messages.success(request, "Multa eliminada.")
    #     return redirect('lista_libros')
    # return render(request, 'libro/confirmar_eliminacion.html', {'multa': multa})
    return render(request, "libro/confirmar_eliminacion.html")
