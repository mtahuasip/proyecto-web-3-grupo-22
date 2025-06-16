from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Prestamo
from .forms import PrestamoForm
from datetime import date
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test

def es_admin(user):
    return not hasattr(user, "socio")

@login_required(login_url="admin_login")
@user_passes_test(es_admin, login_url="/")
def listar_prestamo(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'prestamo/lista_prestamo.html', {'prestamos': prestamos})

@login_required(login_url="admin_login")
@user_passes_test(es_admin, login_url="/")
def detalle_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    return render(request, 'prestamo/detalle_prestamo.html', {'prestamo': prestamo})

@login_required(login_url="admin_login")
@user_passes_test(es_admin, login_url="/")
def agregar_prestamo(request):
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.save()
            messages.success(request, "Préstamo agregado correctamente.")
            return redirect('listar_prestamo')
    else:
        form = PrestamoForm()
    return render(request, 'prestamo/formulario_prestamo.html', {'form': form})

@login_required(login_url="admin_login")
@user_passes_test(es_admin, login_url="/")
def editar_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    if request.method == "POST":
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.save()
            messages.success(request, "Préstamo actualizado correctamente.")
            return redirect('listar_prestamo')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'prestamo/formulario_prestamo.html', {'form': form})

@login_required(login_url="admin_login")
@user_passes_test(es_admin, login_url="/")
def eliminar_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    if request.method == "POST":
        prestamo.delete()
        return JsonResponse({"mensaje": "Préstamo eliminado correctamente."})
    return render(request, 'prestamo/eliminar_prestamo.html', {'prestamo': prestamo})

@login_required(login_url="admin_login")
@user_passes_test(es_admin, login_url="/")
def devolver_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    if request.method == "POST":
        prestamo.fecha_devolucion = request.POST.get('fecha_devolucion') or date.today()
        prestamo.save()
        messages.success(request, "El libro ha sido devuelto correctamente.")
        return redirect('detalle_prestamo', prestamo_id=prestamo.id)
    return render(request, 'prestamo/devolver_prestamo.html', {'prestamo': prestamo})