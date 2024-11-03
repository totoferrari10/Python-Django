from django.http import HttpResponse
from django.template import Template, Context, loader
from django.urls import reverse
from urllib.parse import urlencode
#RUTA PARA USAR UN TEMPLATE👇
from django.shortcuts import render, redirect
#RUTA PARA USAR 
from .models import Coworking
from inicio.forms import listarEspaciosForms
from inicio.forms import buscarEspaciosForms






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

from django.contrib import messages

def listar_espacios(request):
    formulario = listarEspaciosForms(request.GET or None)

    
    if formulario.is_valid():  # Si el formulario es válido
        # Obtenemos los datos del formulario
        nombre = formulario.cleaned_data.get("nombre")
        capacidad = formulario.cleaned_data.get("capacidad")
        
        # Construimos la URL para `buscar_espacios` con los parámetros
        query_params = f"?nombre={nombre}&capacidad={capacidad}"
        buscar_espacios_url = reverse("inicio:buscar_espacios") + query_params
        messages.success(request, f"Tu lugar fue guardado a nombre de {nombre} para una capacidad de {capacidad} personas.")
        
        return redirect(buscar_espacios_url)

    return render(request, 'inicio/listar_espacios.html', {'form': formulario})



def buscar_espacios(request):
    # Inicializamos el formulario con los datos GET para mostrar en la página
    formulario = buscarEspaciosForms(request.GET or None)
    espacios = Coworking.objects.all()
    
    # Comprobamos si tenemos parámetros de búsqueda
    if formulario.is_valid():
        nombre = formulario.cleaned_data.get("nombre")
        capacidad = formulario.cleaned_data.get("capacidad")
        
        # Filtramos por nombre y capacidad si esos campos tienen valores
        if nombre:
            espacios = espacios.filter(nombre__icontains=nombre)
        if capacidad:
            espacios = espacios.filter(capacidad=capacidad)
    return render(request, 'inicio/buscar_espacios.html', {'formulario': formulario, 'espacios': espacios})

def sobre_nosotros(request):
    return render(request, 'inicio/sobre_nosotros.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactoForm

def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("name")
        email = request.POST.get("email")
        telefono = request.POST.get("phone")
        mensaje = request.POST.get("message")
        
        # Aquí puedes añadir código para enviar el mensaje por email, guardar en la base de datos, etc.

        messages.success(request, "El formulario fue enviado con éxito!")
        return redirect('inicio:contacto')  # Cambia este nombre de vista por la correcta

    return render(request, "inicio/contacto.html")






