from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("catalogo/", views.catalogo, name="catalogo"),
    path("catalogo/libro/<int:pk>/", views.catalogo_libro, name="catalogo_libro"),
]
