from django.shortcuts import render
from static.hotel.bd.connection import conn


# Create your views here.


def suites():
    with conn.cursor() as read:
        sql = "select id, identifica from tb_suites where sit = 1"
        read.execute(sql)
        suites = read.fetchall()
        read.close()
    return suites


def reserva():
    with conn.cursor() as read:
        sql = "select * from tb_reservas"
        read.execute(sql)
        dados = read.fetchall()
        read.close()
    return dados


def cliente():
    with conn.cursor() as read:
        sql = "select id, name from tb_clientes"
        read.execute(sql)
        clientes = read.fetchall()
        read.close()
    return clientes


def adicionaReserva(request):

    with conn.cursor() as read:
        sql = "select * from tb_suites where sit = 0"
        read.execute(sql)
        dados2 = read.fetchall()
        read.close()
    return render(request, 'reservas/cadReservas.html', {'dados': cliente(), 'dados2': dados2})


def listaReserva(request):
    return render(request, 'reservas/listaReservas.html', {'dados': reserva(), 'clientes': cliente(), 'suites': suites()})


def inserirReserva(request):
    cliente = request.POST['cliente']
    data = request.POST['data']
    data2 = request.POST['data2']
    quarto = request.POST['quarto']
    try:
        with conn.cursor() as insere:
            sql = "insert into tb_reservas(cliente,data_ini,data_end,quarto) values (%s, %s, %s, %s)"
            insere.execute(sql, (cliente, data, data2, quarto))
            insere.close()
            conn.commit()
        return render(request, 'reservas/listaReservas.html')
    except:
        return render(request, 'reservas/listaReservas.html')


def reservaDelete(request, id):
    with conn.cursor() as delete:
        sql = "delete from tb_reservas where id = %s"
        delete.execute(sql, id)
        conn.commit()
        delete.close()
    return render(request, 'reservas/listaReservas.html',
                  {'dados': reserva(), 'clientes': cliente(), 'suites': suites()})


def reservaEdit(request, id):
    return render(request, 'reservas/listaReservas.html',
                  {'dados': reserva(), 'clientes': cliente(), 'suites': suites()})


def changeSit(request, id):
    return render(request, 'reservas/listaReservas.html',
                  {'dados': reserva(), 'clientes': cliente(), 'suites': suites()})


def editReserva(request, id):
    with conn.cursor() as read:
        sql = "select * from tb_reservas where id = %s"
        read.execute(sql, id)
        dados = read.fetchall()
        read.close()
    return render(request, 'reservas/edit_reservas.html', {'dados': dados})
