from django.urls import path
from . import views
from home.views import index
urlpatterns = [
    path('cadClientes/', views.listaCliente, name='clientes'),
    path('', views.cadCliente, name='inserir'),
    path('listagem/', views.listCliente, name='lista_cliente'),
    path('', index, name='home'),
]
