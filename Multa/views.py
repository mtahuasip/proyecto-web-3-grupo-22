from django.shortcuts import render
from django.http import HttpResponse


def listar_multas(request):
    return HttpResponse("Lista todas las multas")


def detalle_multa(request, id):
    return HttpResponse(f"Detalle multa {id}")


def agregar_multa(request):
    return HttpResponse("Agregar multa")


def editar_multa(request, id):
    return HttpResponse(f"Editar multa {id}")


def eliminar_multa(request, id):
    return HttpResponse(f"Elimina multa {id}")
