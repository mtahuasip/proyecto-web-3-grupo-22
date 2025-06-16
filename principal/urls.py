from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("catalogo/", views.catalogo, name="catalogo"),
    path("catalogo/libro/<int:pk>/", views.catalogo_libro, name="catalogo_libro"),
    path("login/admin/", views.admin_login, name="admin_login"),
    path("socios/registro/", views.socios_registro, name="socios_registro"),
    path("socios/login/", views.socios_login, name="socios_login"),
    path("usuarios/logout/", views.usuarios_logout, name="usuarios_logout"),
    path("catalogo/socios/prestamos/", views.socios_prestamos, name="socios_prestamos"),
    path("catalogo/socios/multas/", views.socios_multas, name="socios_multas"),
]
