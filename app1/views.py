from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from .models import Curso
import datetime


# Create your views here.


def probandoTemplate(request):
   
    nom = "Nicolas"
    ap = "Perez"
   
    lista_de_notas = [1,2,3,5,8,3,2]
    diccionario = {"nombre": nom, "apellido": ap, "hoy": datetime.datetime.now(), "notas": lista_de_notas} # <---- Para enviar al contexto
   
    mi_html = open("C:/Users/mteti/Documents/Coderhouse/Python/Proyecto/proyecto_mati/Template/Template.html")
   
    plantilla = Template(mi_html.read()) # Se carga en memoria nuestro documento
    # OJO: Importar Template y Context con: from django.template import Template, Context
   
    mi_html.close() # Cerramos el archivo
   
    mi_contexto = Context(diccionario) # Le doy al contexto mi nombre y apellido
    documento = plantilla.render(mi_contexto) # Aca renderizamos la plantilla en documento

    return HttpResponse(documento)

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
