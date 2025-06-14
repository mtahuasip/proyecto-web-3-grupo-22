from django.shortcuts import render


def inicio(request):
    return render(request, "principal/inicio.html")


def login_admin(request):
    return render(request, "principal/login_admin.html")
