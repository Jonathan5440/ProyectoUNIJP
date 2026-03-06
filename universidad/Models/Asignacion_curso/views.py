from django.shortcuts import render, get_object_or_404, redirect
from .models import Asignacion_curso
from universidad.Models.Curso.models import Curso
from universidad.Models.Catedratico.models import Catedratico

def asignacion_list(request):
    asignaciones = Asignacion_curso.objects.all()
    return render(request, 'asignacion_curso/list.html', {'asignaciones': asignaciones})

def asignacion_create(request):
    if request.method == 'POST':
        Asignacion_curso.objects.create(
            curso_id=request.POST['curso'],
            catedratico_id=request.POST['catedratico'],
            horario=request.POST['horario']
        )
        return redirect('asignacion_list')
    cursos = Curso.objects.all()
    catedraticos = Catedratico.objects.all()
    return render(request, 'asignacion_curso/form.html', {'cursos': cursos, 'catedraticos': catedraticos})

def asignacion_edit(request, pk):
    asignacion = get_object_or_404(Asignacion_curso, pk=pk)
    if request.method == 'POST':
        asignacion.curso_id = request.POST['curso']
        asignacion.catedratico_id = request.POST['catedratico']
        asignacion.horario = request.POST['horario']
        asignacion.save()
        return redirect('asignacion_list')
    cursos = Curso.objects.all()
    catedraticos = Catedratico.objects.all()
    return render(request, 'asignacion_curso/form.html', {'asignacion': asignacion, 'cursos': cursos, 'catedraticos': catedraticos})

def asignacion_delete(request, pk):
    asignacion = get_object_or_404(Asignacion_curso, pk=pk)
    asignacion.delete()
    return redirect('asignacion_list')