from django.urls import path
from . import views
from home.views import index

urlpatterns = [
    path('listaClientes/', views.adicionaReserva, name='clientes'),
    path('listaClientes/', views.listaReserva, name='clientes'),
    path('', index, name='home'),
]
