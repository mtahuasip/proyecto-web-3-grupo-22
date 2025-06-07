from django.urls import path
from . import views

urlpatterns = [
    path("listar/", views.listar_multas, name="listar_multar"),
    path("detalle/<int:id>/", views.detalle_multa, name="detalle_multa"),
    path("agregar/", views.agregar_multa, name="agregar_multa"),
    path("editar/<int:id>/", views.editar_multa, name="editar_multa"),
    path("eliminar/<int:id>/", views.eliminar_multa, name="eliminar_multa"),
]
