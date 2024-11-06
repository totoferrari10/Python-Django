

from django.urls import path
from inicio import views

app_name = "inicio"

urlpatterns = [

    path('', views.inicio, name="inicio"),
    path('segundo-template/', views.segundo_template, name='segundo_template'),
    path('espacios/', views.listar_espacios, name='listar_espacios'),
    path('buscar/', views.buscar_espacios, name='buscar_espacios'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('contacto/', views.contacto, name='contacto'),



]

