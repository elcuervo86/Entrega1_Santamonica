
from django.urls import path
from AppDisqueria import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('vinilos', views.vinilos, name="Vinilos"),
    path('cds', views.cds, name="CDs"),
    path('clientes', views.clientes, name="Clientes")
   
]
