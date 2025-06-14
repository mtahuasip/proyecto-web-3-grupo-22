from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("login/admin/", views.login_admin, name="login_admin"),
]
