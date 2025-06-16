from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import SocioRegistroForm, SocioLoginForm
from Libro.models import Libro
from socios.models import Socio


def es_socio(user):
    return hasattr(user, "socio")


def inicio(request):
    return render(request, "principal/inicio.html")


def catalogo(request):
    libros = Libro.objects.all()
    return render(request, "principal/catalogo.html", {"libros": libros})


def catalogo_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, "principal/catalogo_libro.html", {"libro": libro})


def socios_login(request):
    if request.method == "POST":
        form = SocioLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            print("valid")
            print(email)
            print(password)

            try:
                username = User.objects.get(email=email).username
                print("usuario encontrado")
                print(username)

                user = authenticate(username=username, password=password)
                if not user:
                    print("Credenciales inválidas.")
                else:
                    print(f"creando sesión para {username}")
                    login(request, user)
                    return redirect("socios_inicio")
            except User.DoesNotExist:
                print("Usuario no encontrado.")

        else:
            print("invalid")
            print(form)
            print(form.cleaned_data["password"])
    else:
        form = SocioLoginForm()
    return render(request, "principal/socios_login.html", {"form": form})


def socios_registro(request):
    if request.method == "POST":
        form = SocioRegistroForm(request.POST)
        if form.is_valid():
            # Crear usuario
            user = User.objects.create_user(
                username=form.cleaned_data["email"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                is_active=True,
                is_staff=False,
                is_superuser=False,
            )

            # Crear perfil de socio
            socio = Socio.objects.create(
                user=user,
                ci=form.cleaned_data["ci"],
                direccion=form.cleaned_data["direccion"],
                celular=form.cleaned_data["celular"],
            )

            messages.success(request, "Registro exitoso. Ahora puedes iniciar sesión.")
            return redirect("socios_login")
    else:
        form = SocioRegistroForm()

    return render(request, "principal/socios_registro.html", {"form": form})


@login_required
@user_passes_test(es_socio)
def socios_logout(request):
    logout(request)
    return redirect("socios_login")
