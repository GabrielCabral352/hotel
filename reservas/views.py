from django.shortcuts import render

# Create your views here.


def adicionaReserva(request):
    return render(request, 'reservas/cadReservas.html')


def listaReserva(request):
    return render(request, 'reservas/listaReservas.html')
