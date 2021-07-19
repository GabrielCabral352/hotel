from django.shortcuts import render
from home.views import index
# Create your views here.
from static.hotel.bd.connection import conn


def listaCliente(request):
    return render(request, 'cliente/index.html')


def cadCliente(request):
    try:
        email = request.POST['email']
        name = request.POST['name']
        cpf = request.POST['cpf']
        password = request.POST['password']

        with conn.cursor() as insere:
            sql = "insert into tb_clientes(name,email,cpf,senha) values (%s, %s, %s, %s)"
            insere.execute(sql, (name, email, cpf, password))
            insere.close()
            conn.commit()
        return render(request, 'cliente/index.html')
    except:
        pass


def listCliente(request):
    with conn.cursor() as read:
        sql = "select * from tb_clientes"
        read.execute(sql)
        dados = read.fetchall()
        read.close()
    return render(request, 'cliente/load_clientes.html', {'dados': dados})


def clienteDelete(request, id):
    with conn.cursor() as delete:
        sql = "delete from tb_clientes where id = %s"
        delete.execute(sql, id)
        conn.commit()
        delete.close()
    return render(request, 'cliente/load_clientes.html')

