import mysql.connector

db =mysql.connector.connect(
    host='localhost',
    user='root',
    password='juan2001%',
    database='blog',
    port=3306
)

'''
#hacer una consulta hay que crear un cursor
cursor=db.cursor()

cursor.execute('select * from usuarios')
print(cursor.fetchall())#retorna los resultados de los datos optenidos'''

def crearUsuario(nombre,email,contacena):
    cursor=db.cursor()
    cursor.execute('''insert into usuarios(nombre,email,contrasena) 
    values(%s,%s,%s)''',(nombre,email,contacena))
    cursor.close()

#creacion, modificacion, eliminacion de datos

crearUsuario("hely","dhwh@hotmnnaig.com","123242")
db.commit()



cursor = db.cursor()

cursor.execute('select * from usuarios')

usuarios = cursor.fetchall()

print(usuarios) 
