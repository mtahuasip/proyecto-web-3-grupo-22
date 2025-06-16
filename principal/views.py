from datetime import date, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import SocioRegistroForm, SocioLoginForm, FechaDevolucionForm
from Libro.models import Libro
from socios.models import Socio
from prestamo.models import Prestamo
from fine.models import Multa


def es_socio(user):
    return hasattr(user, "socio")


def inicio(request):
    return render(request, "principal/inicio.html")


def catalogo(request):
    libros = Libro.objects.all()
    return render(request, "principal/catalogo.html", {"libros": libros})


def catalogo_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == "POST":
        form = FechaDevolucionForm(request.POST)
        if form.is_valid():
            fecha_devolucion = form.cleaned_data.get("fecha_devolucion")
            print(fecha_devolucion)
            print(libro)
            socio = request.user.socio
            print(socio)
            fecha_limite = fecha_devolucion + timedelta(weeks=1)
            print(fecha_limite)
            try:
                prestamo = Prestamo.objects.create(
                    libro=libro,
                    socio=socio,
                    fecha_pretamo=date.today(),
                    fecha_devolucion=fecha_devolucion,
                    fecha_limite=fecha_limite,
                )
                print(prestamo)
                libro.disponibilidad = False
                libro.save()

                messages.success(request, "¡Préstamo realizado con éxito!")
                return redirect("catalogo_libro", pk=libro.pk)
            except:
                print("error")
    else:
        form = FechaDevolucionForm()
    return render(
        request,
        "principal/catalogo_libro.html",
        {
            "libro": libro,
            "form": form,
        },
    )


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
                    return redirect("catalogo")
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
def usuarios_logout(request):
    logout(request)
    return redirect("/")


def socios_prestamos(request):
    socio = Socio.objects.get(user=request.user)
    prestamos = Prestamo.objects.filter(socio=socio).select_related("libro")

    return render(request, "principal/socios_prestamos.html", {"prestamos": prestamos})


def socios_multas(request):
    socio = Socio.objects.get(user=request.user)
    multas = Multa.objects.filter(socio=socio).select_related("prestamo__libro")

    return render(request, "principal/socios_multas.html", {"multas": multas})
