from django.shortcuts import render, redirect
from .models import Socio
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import SocioEditarForm  
from django.contrib.auth.decorators import user_passes_test
    
def es_superusuario(user):
    return user.is_superuser
@user_passes_test(es_superusuario)
def lista_socios(request):
    
    socios = Socio.objects.all()
    return render(request, 'socios/lista_socios.html', {'socios': socios})

@user_passes_test(es_superusuario)
def detalle_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    return render(request, 'socios/detalle_socio.html', {'socio': socio})

@user_passes_test(es_superusuario)
def eliminar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    if request.method == "POST":
        socio.delete()
        messages.success(request, "Socio eliminado correctamente.")
        return redirect('lista_socios') 
    return render(request, 'socios/confirmar_eliminacion.html', {'socio': socio})

@user_passes_test(es_superusuario)
def editar_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)

    if request.method == 'POST':
        form = SocioEditarForm(request.POST, instance=socio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Socio actualizado correctamente.')
            return redirect('detalle_socio', pk=socio.pk)
    else:
        form = SocioEditarForm(instance=socio)

    return render(request, 'socios/editar_socio.html', {'form': form, 'socio': socio})