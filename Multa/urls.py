from django.urls import path
from . import views

urlpatterns = [
    path("lista/", views.lista_multas, name="lista_multas"),
    path("detalle/<int:id>/", views.detalle_multa, name="detalle_multa"),
    path("crear/", views.crear_multa, name="crear_multa"),
    path("editar/<int:id>/", views.editar_multa, name="editar_multa"),
    path("eliminar/<int:id>/", views.eliminar_multa, name="eliminar_multa"),
]
