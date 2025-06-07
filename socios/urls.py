from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registrar_socio, name='registro_socio'),
    path('socios/', views.lista_socios, name='lista_socios'),
    path('eliminar/<int:socio_id>/', views.eliminar_socio, name='eliminar_socio'),]