from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from .models import Curso

# Create your views here.

def probandoTemplate(self):
    mi_html = open("C:/Users/mteti/Documents/Coderhouse/Python/Proyecto/proyecto_mati/Template/Template.html")
    
    plantilla = Template(mi_html.read())

    mi_html.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)

def curso_list(request):
    curso = Curso.objects.all()
    return render(request, 'curso_list.html', {'curso':curso})

def curso_create(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero_comision = request.POST.get('numero_comision')
        curso = Curso(nombre=nombre, numero_comision=numero_comision)
        curso.save()
        return redirect('curso_list')
    
    return render(request, 'curso_create.html')