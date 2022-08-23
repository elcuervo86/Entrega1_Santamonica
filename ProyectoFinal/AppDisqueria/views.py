from django.shortcuts import render

# Create your views here.
def inicio(request):

      return render(request, "AppDisqueria/inicio.html")

def vinilos(request):

      return render(request, "AppDisqueria/vinilos.html")

def cds(request):

      return render(request, "AppDisqueria/cds.html")


def clientes(request):

      return render(request, "AppDisqueria/clientes.html")