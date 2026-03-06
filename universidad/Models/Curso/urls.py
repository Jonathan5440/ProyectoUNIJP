from django.urls import path
from . import views

urlpatterns = [
    path('', views.curso_list, name='curso_list'),
    path('crear/', views.curso_create, name='curso_create'),
    path('editar/<int:pk>/', views.curso_edit, name='curso_edit'),
    path('eliminar/<int:pk>/', views.curso_delete, name='curso_delete'),
]