import pymysql.cursors

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='habbo_hotel',
        cursorclass=pymysql.cursors.DictCursor
    )

except:
    print("Falha ao conectar com o banco de dados")


