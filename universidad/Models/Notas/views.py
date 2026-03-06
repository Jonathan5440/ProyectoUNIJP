from django.shortcuts import render, get_object_or_404, redirect
from .models import Notas
from universidad.Models.Inscripcion_alumno.models import Inscripcion_alumno

def notas_list(request):
    notas = Notas.objects.all()
    return render(request, 'notas/list.html', {'notas': notas})

def notas_create(request):
    if request.method == 'POST':
        Notas.objects.create(
            inscripcion_id=request.POST['inscripcion'],
            nota=request.POST['nota'],
            descripcion=request.POST.get('descripcion', '')
        )
        return redirect('notas_list')
    inscripciones = Inscripcion_alumno.objects.all()
    return render(request, 'notas/form.html', {'inscripciones': inscripciones})

def notas_edit(request, pk):
    nota = get_object_or_404(Notas, pk=pk)
    if request.method == 'POST':
        nota.inscripcion_id = request.POST['inscripcion']
        nota.nota = request.POST['nota']
        nota.descripcion = request.POST.get('descripcion', '')
        nota.save()
        return redirect('notas_list')
    inscripciones = Inscripcion_alumno.objects.all()
    return render(request, 'notas/form.html', {'nota': nota, 'inscripciones': inscripciones})

def notas_delete(request, pk):
    nota = get_object_or_404(Notas, pk=pk)
    nota.delete()
    return redirect('notas_list')