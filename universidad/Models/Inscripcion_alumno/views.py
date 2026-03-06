from django.shortcuts import render, get_object_or_404, redirect
from .models import Inscripcion_alumno
from universidad.Models.Alumno.models import Alumno
from universidad.Models.Asignacion_curso.models import Asignacion_curso

def inscripcion_list(request):
    inscripciones = Inscripcion_alumno.objects.all()
    return render(request, 'inscripcion_alumno/list.html', {'inscripciones': inscripciones})

def inscripcion_create(request):
    if request.method == 'POST':
        Inscripcion_alumno.objects.create(
            alumno_id=request.POST['alumno'],
            asignacion_id=request.POST['asignacion']
        )
        return redirect('inscripcion_list')
    alumnos = Alumno.objects.all()
    asignaciones = Asignacion_curso.objects.all()
    return render(request, 'inscripcion_alumno/form.html', {'alumnos': alumnos, 'asignaciones': asignaciones})

def inscripcion_edit(request, pk):
    inscripcion = get_object_or_404(Inscripcion_alumno, pk=pk)
    if request.method == 'POST':
        inscripcion.alumno_id = request.POST['alumno']
        inscripcion.asignacion_id = request.POST['asignacion']
        inscripcion.save()
        return redirect('inscripcion_list')
    alumnos = Alumno.objects.all()
    asignaciones = Asignacion_curso.objects.all()
    return render(request, 'inscripcion_alumno/form.html', {'inscripcion': inscripcion, 'alumnos': alumnos, 'asignaciones': asignaciones})

def inscripcion_delete(request, pk):
    inscripcion = get_object_or_404(Inscripcion_alumno, pk=pk)
    inscripcion.delete()
    return redirect('inscripcion_list')