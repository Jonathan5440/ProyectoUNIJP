from django.shortcuts import render, get_object_or_404, redirect
from .models import Catedratico

def catedratico_list(request):
    catedraticos = Catedratico.objects.all()
    return render(request, 'catedratico/list.html', {'catedraticos': catedraticos})

def catedratico_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST.get('phone', '')
        Catedratico.objects.create(first_name=first_name, last_name=last_name, email=email, phone=phone)
        return redirect('catedratico_list')
    return render(request, 'catedratico/form.html')

def catedratico_edit(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)
    if request.method == 'POST':
        catedratico.first_name = request.POST['first_name']
        catedratico.last_name = request.POST['last_name']
        catedratico.email = request.POST['email']
        catedratico.phone = request.POST.get('phone', '')
        catedratico.save()
        return redirect('catedratico_list')
    return render(request, 'catedratico/form.html', {'catedratico': catedratico})

def catedratico_delete(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)
    catedratico.delete()
    return redirect('catedratico_list')