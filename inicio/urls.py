

from django.urls import path
from inicio.views import mi_vista, inicio, vistas_datos1, segundo_template, primer_template

urlpatterns = [
    path("mi-vista/", mi_vista),
    path('', inicio),  
    path("vista-datos1/", vistas_datos1),
    path("segundo-template/", segundo_template), 
    path("primer-template/", primer_template)  
]