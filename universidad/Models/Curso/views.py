from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/list.html', {'cursos': cursos})

def curso_create(request):
    if request.method == 'POST':
        Curso.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST.get('descripcion', ''),
            creditos=request.POST['creditos']
        )
        return redirect('curso_list')
    return render(request, 'curso/form.html')

def curso_edit(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.nombre = request.POST['nombre']
        curso.descripcion = request.POST.get('descripcion', '')
        curso.creditos = request.POST['creditos']
        curso.save()
        return redirect('curso_list')
    return render(request, 'curso/form.html', {'curso': curso})

def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    curso.delete()
    return redirect('curso_list')