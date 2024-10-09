from django.http import HttpResponse
from django.template import Template, Context, loader
#RUTA DE FECHA Y HORA ACTUAL
from datetime import datetime
#RUTA PARA USAR UN TEMPLATE👇
from django.shortcuts import render

def mi_vista(request):
    return HttpResponse( "Hola soy la vista" )

def inicio(request):
    return HttpResponse( '<h1>Hola estamos en el inicio</h1>' )

def vistas_datos1(request):
    return HttpResponse( "Hola!!!" )


#################################TEMPLATE 1
def primer_template(request):
    # con with
    with open(r'templates\primer_template.html') as archivo_del_template:
        template = Template(archivo_del_template.read())
    
    contexto = Context()
    
    render_template = template.render(contexto)
    
    return HttpResponse(render_template)


#################################TEMPLATE 2
def segundo_template(request):
    
    #FUNCION DE FECHA Y HORA ACTUAL
    fecha_actual = datetime.now()
    datos = {"fecha_actual": fecha_actual,
                    "numeros": list(range(1,11))
            }
    
#VERSION 3 y definitiva de COMO usar un TEMPLATE
    return render(request, "segundo_template.html", datos)