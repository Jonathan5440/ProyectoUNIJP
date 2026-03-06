from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('alumnos/', include('universidad.Models.Alumno.urls')),
    path('catedraticos/', include('universidad.Models.Catedratico.urls')),
    path('cursos/', include('universidad.Models.Curso.urls')),
    path('asignaciones/', include('universidad.Models.Asignacion_curso.urls')),
    path('inscripciones/', include('universidad.Models.Inscripcion_alumno.urls')),
    path('notas/', include('universidad.Models.Notas.urls')),
]