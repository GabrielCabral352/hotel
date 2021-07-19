from django.urls import path
from . import views
from home.views import index

urlpatterns = [
    path('cadReserva/', views.adicionaReserva, name='reserva'),
]
