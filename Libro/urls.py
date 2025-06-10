from django.urls import path
from . import views

urlpatterns = [
    path("lista/", views.lista_libros, name="lista_libros"),
    path("detalle/<int:id>/", views.detalle_libro, name="detalle_libro"),
    path("crear/", views.crear_libro, name="crear_libro"),
    path("editar/<int:id>/", views.editar_libro, name="editar_libro"),
   path('libros/eliminar/<int:id>/', views.eliminar_libro, name='eliminar_libro'),

]
