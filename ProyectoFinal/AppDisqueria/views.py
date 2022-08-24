import email
from email.message import EmailMessage
import mailbox
from msilib.schema import CheckBox
from tabnanny import check
from tokenize import Number
from unicodedata import numeric
from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppDisqueria.models import Vinilo, cd, Cliente
from AppDisqueria.forms import ViniloForm, CdForm, ClienteForm

# Create your views here.
def inicio(request):

      return render(request, "AppDisqueria/inicio.html")

#VINILOS      

def vinilos(request):

      return render(request, "AppDisqueria/vinilos.html")

#def vinilosForm(request):

     # return render(request, "AppDisqueria/vinilosForm.html")

def vinilosForm(request):

      if request.method == "POST":

            miFormulario = ViniloForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  vinilo = Vinilo(banda=informacion["banda"], nombreDisco=informacion["nombreDisco"], precio=informacion["precio"], indNacional=CheckBox["IndNacional"])
                  vinilo.save()
                  return render(request, "AppDisqueria/inicio.html")
      else:
            miFormulario = ViniloForm()

      return render(request, "AppDisqueria/vinilosForm.html", {"miFormulario": miFormulario})

#CDS

def cds(request):

      return render(request, "AppDisqueria/cds.html")

def cdsForm(request):

      return render(request, "AppDisqueria/cdsForm.html")


#CLIENTES

def clientes(request):

      return render(request, "AppDisqueria/clientes.html")

#def clientesForm(request):

 #     return render(request, "AppDisqueria/clientesForm.html")

def clientesForm(request):

      if request.method == "POST":

            miFormulario = ClienteForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], telefono=Number['telefono'])
                  cliente.save()
                  return render(request, "AppDisqueria/inicio.html")
      else:
            miFormulario = ClienteForm()

      return render(request, "AppDisqueria/clientesForm.html", {"miFormulario": miFormulario})