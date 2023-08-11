from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from .models import Curso
import datetime


# Create your views here.


def index(request):
    return render(request, 'index.html')

def curso_list(request):
    curso = Curso.objects.all()
    return render(request, 'curso_list.html', {'curso' : curso})

def curso_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero_comision = request.POST.get('numero_comision')
        curso = Curso(nombre=nombre, numero_comision=numero_comision)
        curso.save()
        return redirect('curso_list')
     
    return render(request, 'curso_create.html')
