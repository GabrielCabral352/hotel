from django.shortcuts import render
from home.views import index
# Create your views here.
from static.hotel.bd.connection import conn


def listaCliente(request):
    return render(request, 'cliente/index.html')


def cadCliente(request):
    email = request.POST['email']
    name = request.POST['name']
    cpf = request.POST['cpf']
    password = request.POST['password']

    with conn.cursor() as insere:
        sql = "insert into tb_clientes(name,email,cpf,senha) values (%s, %s, %s, %s)"
        insere.execute(sql, (email, name, cpf, password))
        insere.close()
        conn.commit()
    return render(request, 'cliente/index.html')


def listCliente(request):
    with conn.cursor() as read:
        sql = "select * from tb_clientes"
        read.execute(sql)
        dados = read.fetchall()
    print(dados)
    return render(request, 'cliente/load_clientes.html', {'dados': dados})
