
from django.urls import path
from AppDisqueria import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('vinilos', views.vinilos, name="Vinilos"),
    path('cds', views.cds, name="CDs"),
    path('clientes', views.clientes, name="Clientes"),
    path('leerCliente', views.leerClientes, name = "LeerClientes"),
    #path('editarCliente/<Cliente _nombre>/', views.editarCliente, name="EditarCliente")
    path('leerCd', views.leerCds, name = "LeerCds"),
    #path('editarCliente/<Cliente _nombre>/', views.editarCliente, name="EditarCliente")
    path('leerVinilo', views.leerVinilos, name = "LeerVinilos"),
    #path('editarCliente/<Cliente _nombre>/', views.editarCliente, name="EditarCliente")
   
]
