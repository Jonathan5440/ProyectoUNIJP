from django.shortcuts import render
from django.db.models import Avg, Count
from universidad.Models.Alumno.models import Alumno
from universidad.Models.Curso.models import Curso
from universidad.Models.Catedratico.models import Catedratico
from universidad.Models.Asignacion_curso.models import Asignacion_curso
from universidad.Models.Inscripcion_alumno.models import Inscripcion_alumno
from universidad.Models.Notas.models import Notas

def reporte_cursos(request):
    """
    Reporte 1: Cursos con promedio de notas y total de alumnos inscritos
    """
    cursos = Curso.objects.annotate(
        total_alumnos=Count('asignacion_curso__inscripcion_alumno__alumno', distinct=True),
        promedio_notas=Avg('asignacion_curso__inscripcion_alumno__notas__nota'),
    ).order_by('-total_alumnos')

    return render(request, 'reportes/reporte_cursos.html', {
        'cursos': cursos,
    })


def reporte_catedraticos(request):
    """
    Reporte 2: Catedráticos con total de alumnos y promedio de notas
    """
    catedraticos = Catedratico.objects.annotate(
        total_alumnos=Count('asignacion_curso__inscripcion_alumno__alumno', distinct=True),
        promedio_notas=Avg('asignacion_curso__inscripcion_alumno__notas__nota'),
        total_cursos=Count('asignacion_curso', distinct=True),
    ).order_by('-total_alumnos')

    return render(request, 'reportes/reporte_catedraticos.html', {
        'catedraticos': catedraticos,
    })