from django.shortcuts import render, get_object_or_404, redirect
from fine.models import Multa
from .forms import MultaForm  
from django.contrib import messages

def lista_multas(request):
    multas = Multa.objects.all()
    return render(request, 'fine/lista_multas.html', {'multas': multas})

def detalle_multa(request, id):
    multa = get_object_or_404(Multa, pk=id)
    return render(request, 'fine/detalle_multa.html', {'multa': multa})

def crear_multa(request):
    if request.method == 'POST':
        form = MultaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Multa creada correctamente.")
            return redirect('lista_multas')
    else:
        form = MultaForm()
    return render(request, 'fine/formulario_multa.html', {'form': form, 'accion': 'Crear'})


def editar_multa(request, id):
    multa = get_object_or_404(Multa, id=id)
    if request.method == 'POST':
        form = MultaForm(request.POST, instance=multa)
        if form.is_valid():
            form.save()
            messages.success(request, "Multa actualizada correctamente.")
            return redirect('lista_multas')
    else:
        form = MultaForm(instance=multa)
    return render(request, 'fine/formulario_multa.html', {
        'form': form,
        'accion': 'Editar'
    })
def eliminar_multa(request, id):
    multa = get_object_or_404(Multa, id=id)

    if request.method == 'POST':
        multa.delete()
        messages.success(request, "Multa eliminada correctamente.")
        return redirect('lista_multas')

    return render(request, 'fine/confirmar_eliminacion.html', {'multa': multa})