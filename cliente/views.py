from django.shortcuts import render
from home.views import index
# Create your views here.


def listaCliente(request):
    return render(request, 'cliente/index.html')

