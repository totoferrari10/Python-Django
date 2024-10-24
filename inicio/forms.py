from django import forms

class listarEspaciosForms(forms.Form):
    nombre = forms.CharField(max_length=20)
    ambientes = forms.IntegerField()
    capacidad = forms.IntegerField()
    mensaje = forms.CharField(max_length=70)  
