from django.urls import path
from . import views
from home.views import index

urlpatterns = [
    path('cadReserva/', views.adicionaReserva, name='reserva'),
    path('', views.inserirReserva, name='fazer_reserva'),
    path('listaReserva/', views.listaReserva, name='lista_reservas'),
]
