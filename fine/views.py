from django.shortcuts import render, get_object_or_404, redirect
from fine.models import Multa
from .forms import MultaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def lista_multas(request):
    query = request.GET.get('q')  # Obtiene el término de búsqueda del query string
    if query:
        multas = Multa.objects.filter(socio__nombre__icontains=query)
    else:
        multas = Multa.objects.all()
    return render(request, 'fine/lista_multas.html', {'multas': multas, 'query': query})

def detalle_multa(request, id):
    multa = get_object_or_404(Multa, pk=id)
    return render(request, 'fine/detalle_multa.html', {'multa': multa})

@login_required
def crear_multa(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    if request.method == 'POST':
        form = MultaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Multa creada correctamente.")
            return redirect('lista_multas')
    else:
        form = MultaForm()
    return render(request, 'fine/formulario_multa.html', {'form': form, 'accion': 'Crear'})

@login_required
def editar_multa(request, id):
    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    multa = get_object_or_404(Multa, id=id)
    if request.method == 'POST':
        form = MultaForm(request.POST, instance=multa)
        if form.is_valid():
            form.save()
            messages.success(request, "Multa actualizada correctamente.")
            return redirect('lista_multas')
    else:
        form = MultaForm(instance=multa)
    return render(request, 'fine/formulario_multa.html', {'form': form, 'accion': 'Editar'})

@login_required
def eliminar_multa(request, id):
    if not request.user.is_staff and not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    multa = get_object_or_404(Multa, id=id)
    if request.method == 'POST':
        multa.delete()
        messages.success(request, "Multa eliminada correctamente.")
        return redirect('lista_multas')
    return render(request, 'fine/confirmar_eliminacion.html', {'multa': multa})
