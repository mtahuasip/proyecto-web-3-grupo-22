from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import Socio
from .forms import SocioForm

def registrar_socio(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)  
        if form.is_valid():
            socio = form.save(commit=False)
            socio.contraseña = make_password(socio.contraseña)
            socio.save()
            return redirect('login_socio')  
    else:
        form = SocioForm()
    return render(request, 'socios/registro_socio.html', {'form': form})


def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'socios/lista_socios.html', {'socios': socios})

def eliminar_socio(request, socio_id):
    try:
        socio = Socio.objects.get(id=socio_id)
        socio.delete()
        return redirect('lista_socios')
    except Socio.DoesNotExist:
        return redirect('lista_socios')  

def login_socio(request):
    error = ""
    if request.method == 'POST':
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']
        try:
            socio = Socio.objects.get(correo=correo)
            if check_password(contraseña, socio.contraseña):
                request.session['socio_id'] = socio.id  
                return redirect('catalogo')  
            else:
                error = "Contraseña incorrecta"
        except Socio.DoesNotExist:
            error = "Correo no registrado"
    return render(request, 'socios/login.html', {'error': error})




