import email
from email.message import EmailMessage
import mailbox
from msilib.schema import CheckBox
from pickletools import int4
from sys import int_info
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

      if request.method == "POST":

            miFormulario = ViniloForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  vinilo = Vinilo(banda=informacion['banda'], nombreDisco=informacion['nombreDisco'], precio=informacion['precio'])
                  vinilo.save()
                  return render(request, "AppDisqueria/inicio.html")
      else:
            miFormulario = ViniloForm()

      return render(request, "AppDisqueria/vinilos.html", {"miFormulario": miFormulario})

def leerVinilos(request):

      vinilos = Vinilo.objects.all() #trae todos los profesores

      contexto= {"vinilos":vinilos} 

      return render(request, "AppDisqueria/leerVinilos.html",contexto)

#CDS

def cds(request):

      if request.method == "POST":

            miFormulario = CdForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  cds = cd(banda=informacion['banda'], nombreDisco=informacion['nombreDisco'], precio=informacion['precio'])
                  cds.save()
                  return render(request, "AppDisqueria/inicio.html")
      else:
            miFormulario = CdForm()

      return render(request, "AppDisqueria/cds.html", {"miFormulario": miFormulario})

def leerCds(request):

      cds = cd.objects.all() #trae todos los profesores

      contexto= {"cds":cds} 

      return render(request, "AppDisqueria/leerCds.html",contexto)

#CLIENTES

def clientes(request):

      if request.method == "POST":

            miFormulario = ClienteForm(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], telefono=informacion['telefono'])
                  cliente.save()
                  return render(request, "AppDisqueria/inicio.html")
      else:
            miFormulario = ClienteForm()

      return render(request, "AppDisqueria/clientes.html", {"miFormulario": miFormulario})
      


def leerClientes(request):

      clientes = Cliente.objects.all() #trae todos los profesores

      contexto= {"clientes":clientes} 

      return render(request, "AppDisqueria/leerClientes.html",contexto)