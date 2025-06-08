from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Socio
from .forms import SocioForm


def registrar_socio(request):
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            socio = form.save(commit=False)
            socio.contrasena = make_password(socio.contrasena)  #  Encriptar contraseña
            socio.save()
            return redirect("lista_socios")
    else:
        form = SocioForm()
    return render(request, "socios/registro_socio.html", {"form": form})


def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, "socios/lista_socios.html", {"socios": socios})


def eliminar_socio(request, socio_id):
    try:
        socio = Socio.objects.get(id=socio_id)
        socio.delete()
        return redirect("lista_socios")
    except Socio.DoesNotExist:
        return redirect("lista_socios")
