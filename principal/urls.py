from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("catalogo/", views.catalogo, name="catalogo"),
    path("catalogo/libro/<int:pk>/", views.catalogo_libro, name="catalogo_libro"),
    path("socios/registro/", views.socios_registro, name="socios_registro"),
    path("socios/login/", views.socios_login, name="socios_login"),
    path("socios/logout/", views.socios_logout, name="socios_logout"),
]
