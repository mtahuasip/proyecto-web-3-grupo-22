from django.urls import path
from .views import listar_prestamo, detalle_prestamo, agregar_prestamo, editar_prestamo, eliminar_prestamo, devolver_prestamo

urlpatterns = [
    path('', agregar_prestamo, name='agregar_prestamo'),
    path('detalle/<int:prestamo_id>/', detalle_prestamo, name='detalle_prestamo'),
    path('lista/', listar_prestamo, name='listar_prestamo'), 
    path('editar/<int:prestamo_id>/', editar_prestamo, name='editar_prestamo'),
    path('eliminar/<int:prestamo_id>/', eliminar_prestamo, name='eliminar_prestamo'),
    path('devolver/<int:prestamo_id>/', devolver_prestamo, name='devolver_prestamo'),

]
