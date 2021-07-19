from django.shortcuts import render
from static.hotel.bd.connection import conn
# Create your views here.


def adicionaReserva(request):
    with conn.cursor() as read:
        sql = "select * from tb_clientes"
        read.execute(sql)
        dados = read.fetchall()
        read.close()

    with conn.cursor() as read:
        sql = "select * from tb_suites where sit = 0"
        read.execute(sql)
        dados2 = read.fetchall()
        read.close()
    return render(request, 'reservas/cadReservas.html', {'dados': dados, 'dados2': dados2})


def listaReserva(request):
    return render(request, 'reservas/listaReservas.html')


def inserirReserva(request):
    cliente = request.POST['cliente']
    data = request.POST['data']
    data2 = request.POST['data2']
    quarto = request.POST['quarto']
    with conn.cursor() as insere:
        sql = "insert into tb_reservas(cliente,data_ini,data_end,quarto) values (%s, %s, %s, %s)"
        insere.execute(sql, (cliente, data, data2, quarto))
        insere.close()
        conn.commit()
    return render(request, 'reservas/listaReservas.html')
