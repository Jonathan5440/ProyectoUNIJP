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
import openpyxl
from django.http import HttpResponse

def exportar_cursos_excel(request):
    cursos = Curso.objects.annotate(
        total_alumnos=Count('asignacion_curso__inscripcion_alumno__alumno', distinct=True),
        promedio_notas=Avg('asignacion_curso__inscripcion_alumno__notas__nota'),
    ).order_by('-total_alumnos')

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Reporte Cursos'

    # Encabezados
    ws.append(['#', 'Curso', 'Créditos', 'Total Alumnos', 'Promedio Notas'])

    # Datos
    for i, curso in enumerate(cursos, 1):
        ws.append([
            i,
            curso.nombre,
            curso.creditos,
            curso.total_alumnos,
            round(curso.promedio_notas, 2) if curso.promedio_notas else 0,
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="reporte_cursos.xlsx"'
    wb.save(response)
    return response


def exportar_catedraticos_excel(request):
    catedraticos = Catedratico.objects.annotate(
        total_alumnos=Count('asignacion_curso__inscripcion_alumno__alumno', distinct=True),
        promedio_notas=Avg('asignacion_curso__inscripcion_alumno__notas__nota'),
        total_cursos=Count('asignacion_curso', distinct=True),
    ).order_by('-total_alumnos')

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Reporte Catedráticos'

    # Encabezados
    ws.append(['#', 'Nombre', 'Email', 'Total Cursos', 'Total Alumnos', 'Promedio Notas'])

    # Datos
    for i, c in enumerate(catedraticos, 1):
        ws.append([
            i,
            f"{c.first_name} {c.last_name}",
            c.email,
            c.total_cursos,
            c.total_alumnos,
            round(c.promedio_notas, 2) if c.promedio_notas else 0,
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename="reporte_catedraticos.xlsx"'
    wb.save(response)
    return response