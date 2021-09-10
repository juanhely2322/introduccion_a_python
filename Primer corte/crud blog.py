

import mysql.connector

base_datos=mysql.connector.connect(
    
    host="localhost",
    user="root",
    password="juan2001%",
    database="blog",
    port=3306
    
    
)

def crearUsuario(nombres,correo,clave):
    cursor=base_datos.cursor()
    cursor.execute('''insert into usuarios(nombre,email,contrasena) 
    values(%s,%s,%s)''',(nombres,correo,clave))
    base_datos.commit()
    cursor.close()


opc=1

while  opc!=5:
            opc=int(input("""
        1. Crear usuario

        2. Leer usuarios

        3. Actualizar un usuario por identificador

        4. eliminar un usuario por identificador 
        """))
            cursor = base_datos.cursor()
            
            if opc==1:
                nombre=input("ingresa nombre del usuario: ")
                email=input ("ingresas el email del usuario")
                contacena=("crea una contraceña")
                crearUsuario(nombre,email,contacena)
            elif opc==2 :
               
                print( cursor.execute('select * from usuarios'))
            elif opc==3 :
                id=input("ingrese id para modificar/actualizar usuario:  ")
                nombre=input("ingrese nuevo nombre: ")
                email=input("ingrese nuevo email: ")
                contrasena=input("ingrese nueva contraseña: ")
                cursor.execute(" update  usuarios set nombre= %s,email=%s,contrasena=%s where id=%s ",(nombre,email,contrasena,id))
                cursor.close()
                base_datos.commit()
                print("¡ACTUALIZACION EXITOSA!")
            elif opc==4:
                 id2=input("ingrese id para eliminar usuario:  ")
                 cursor.execute("delete from usuarios where id=%s",(id2))
                 base_datos.commit()
                 cursor.close()
                
                
                  
        
        
        
        


