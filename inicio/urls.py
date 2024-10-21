

from django.urls import path
from inicio.views import inicio, segundo_template, primer_template, listar_espacios, buscar_espacios

app_name = "inicio"

urlpatterns = [

    path('', inicio, name="inicio"),
    path('segundo-template/', segundo_template, name='segundo_template'),
    path("primer-template/", primer_template, name="primer_template"),
    path('espacios/', listar_espacios, name='listar_espacios'),
    path('buscar/', buscar_espacios, name='buscar_espacios'),

]

