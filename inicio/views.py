from django.http import HttpResponse
from django.template import Template, Context, loader
#RUTA DE FECHA Y HORA ACTUAL
from datetime import datetime
#RUTA PARA USAR UN TEMPLATE👇
from django.shortcuts import render
#RUTA PARA USAR 
from .models import Coworking


def inicio(request):
    return render (request, "inicio/index.html")


#################################TEMPLATE 1
def primer_template(request):
                                                                        ## con with
    with open(r'templates\primer_template.html') as archivo_del_template:
        template = Template(archivo_del_template.read())
    contexto = Context()
    render_template = template.render(contexto)    
    return HttpResponse(render_template)


#################################TEMPLATE 2
def segundo_template(request):    
#VERSION 3 y definitiva de COMO usar un TEMPLATE
    return render(request, "inicio/segundo_template.html")



#################################TEMPLATE 3
def listar_espacios(request):
    espacios = Coworking.objects.all()  # Recupera todos los espacios
    return render(request, 'inicio/listar_espacios.html', {'espacios': espacios})







