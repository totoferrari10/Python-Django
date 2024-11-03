from django import forms
from .models import Contacto

class listarEspaciosForms(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    email = forms.CharField(max_length=70,required=False)  
    ambientes = forms.IntegerField(required=False)
    capacidad = forms.IntegerField(required=False)
    mensaje = forms.CharField(max_length=70,required=False)  


class buscarEspaciosForms(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    capacidad= forms.IntegerField(required=False)
    
class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]