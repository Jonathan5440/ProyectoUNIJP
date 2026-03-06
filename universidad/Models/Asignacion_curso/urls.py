from django.urls import path
from . import views

urlpatterns = [
    path('', views.asignacion_list, name='asignacion_list'),
    path('crear/', views.asignacion_create, name='asignacion_create'),
    path('editar/<int:pk>/', views.asignacion_edit, name='asignacion_edit'),
    path('eliminar/<int:pk>/', views.asignacion_delete, name='asignacion_delete'),
]