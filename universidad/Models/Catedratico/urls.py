from django.urls import path
from . import views

urlpatterns = [
    path('', views.catedratico_list, name='catedratico_list'),
    path('crear/', views.catedratico_create, name='catedratico_create'),
    path('editar/<int:pk>/', views.catedratico_edit, name='catedratico_edit'),
    path('eliminar/<int:pk>/', views.catedratico_delete, name='catedratico_delete'),
]