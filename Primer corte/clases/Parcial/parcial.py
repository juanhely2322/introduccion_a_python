


import mysql.connector
import hashlib

usuario=mysql.connector.connect(
    host='localhost',
    user='root',
    password='juan2001%',
    database='lg4_parcial',
    port=3306
)


def crearUsuario(nombres,correo,clave):
    cursor=usuario.cursor()
    cursor.execute('''insert into usuarios(nombre,email,contrasena) 
    values(%s,%s,%s)''',(nombres,correo,clave,))
    usuario.commit()
    cursor.close()
    

opc=1
cursor=usuario.cursor()
while  opc!=3 and opc<=3:
            opc=int(input("""
        1. Crear usuario

        2. iniciar sesion
        """))
            
            if opc==1:
                nombre=input("ingresa nombre del usuario:  ")
                #cursor.execute('''INSERT into usuarios(nombre) values (s%)''',(nombre))
                email=input ("ingresas su email:")
                #cursor.execute('''INSERT into usuarios(email) values (s%)''',(email))
                contracena= ( input("crea una contraceña: "))
                crearUsuario(nombre,email,contracena)
                    
                
            if opc==2:
                correo=input("ingresa tu correo: ")
                clave= input("ingrese su contraseña: ")
                cursor.execute('''SELECT contrasena from usuarios where contrasena=%s''',(clave))
                contraceña=cursor.fetchall()
                usuario.commit()
                cursor.close()
               
                if contraceña ==clave:
                    print("clave correcta")  
                
        