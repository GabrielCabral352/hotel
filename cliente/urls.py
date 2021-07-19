from django.urls import path
from . import views
from home.views import index
urlpatterns = [
    path('cadClientes/', views.listaCliente, name='clientes'),
    path('', views.cadCliente, name='inserir'),
    path('atualizar/?P<int:id>', views.attCliente, name='atualizar'),
    path('listagem/', views.listCliente, name='lista_cliente'),
    path('delCliente/?P<int:id>', views.clienteDelete, name="delCliente"),
    path('editCliente/?P<int:id>', views.editCliente, name="editCliente"),
    path('', index, name='home'),
]
