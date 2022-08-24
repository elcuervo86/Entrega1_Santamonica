from django import forms


class ViniloForm(forms.Form):
    banda = forms.CharField(max_length=30)
    nombreDisco = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    indNacional = forms.BooleanField()

class CdForm(forms.Form):
    banda = forms.CharField(max_length=30)
    nombreDisco = forms.CharField(max_length=30)
    precio = forms.IntegerField()
    indNacional = forms.BooleanField()

class ClienteForm(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    telefono = forms.IntegerField()