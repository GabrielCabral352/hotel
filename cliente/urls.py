from django.urls import path
from . import views
from home.views import index
urlpatterns = [
    path('listaClientes/', views.listaCliente, name='clientes'),
    path('', index, name='home'),
]
