from django.http import HttpResponse
from django.template import Template, Context, loader
#RUTA PARA USAR UN TEMPLATE👇
from django.shortcuts import render, redirect
#RUTA PARA USAR 
from .models import Coworking
from inicio.forms import listarEspaciosForms


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



################################# Vista del listado de espacios

# def listar_espacios(request, nombre, ambientes, capacidad):
    
#     auto = Coworking(nombre=nombre, ambientes=ambientes, capacidad=capacidad)
#     auto.save()
#     return render(request, 'inicio/listar_espacios.html', {'coworking': Coworking})

# def listar_espacios(request):
#     coworking = Coworking.objects.all()  # Recupera todos los espacios
        
#     print("Request", request)
#     print("GET", request.GET)
#     print("POST", request.POST)
    
#     formulario=listarEspaciosForms()
    
    
#     if request.method == "POST":
#         formulario = listarEspaciosForms(request.POST)
#         if formulario.is_valid():
#             data = formulario.cleaned_data
#             coworking= Coworking(nombre=data.get("nombre"), ambientes=data.get("ambientes"), capacidad=data.get("capacidad"), mensaje=data.get("mensaje"))
#             coworking.save()
#             return redirect("inicio:buscar_espacios")
#     return render(request, 'inicio/listar_espacios.html', { 'form': formulario})



# def buscar_espacios(request):
#     espacios = Coworking.objects.all()
    
#     return render(request, 'inicio/buscar_espacios.html', {'espacios': espacios})

from django.shortcuts import render, redirect
from .models import Coworking
from inicio.forms import listarEspaciosForms

def listar_espacios(request):
    coworking = Coworking.objects.all()  # Recupera todos los espacios
        
    print("Request", request)
    print("GET", request.GET)
    print("POST", request.POST)
    
    formulario = listarEspaciosForms()

    if request.method == "POST":
        formulario = listarEspaciosForms(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            coworking = Coworking(
                nombre=data.get("nombre"),
                ambientes=data.get("ambientes"),
                capacidad=data.get("capacidad"),
                mensaje=data.get("mensaje")
            )
            coworking.save()
            return redirect("inicio:buscar_espacios")
    
    return render(request, 'inicio/listar_espacios.html', {'form': formulario, 'espacios': coworking})

def buscar_espacios(request):
    espacios = Coworking.objects.all()  # Recupera todos los espacios de la base de datos
    return render(request, 'inicio/buscar_espacios.html', {'espacios': espacios})







