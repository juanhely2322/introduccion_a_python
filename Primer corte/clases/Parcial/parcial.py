


import mysql.connector


usuario=mysql.connector.connect(
    host='localhost',
    user='root',
    password='juan2001%',
    database='lg4_parcial',
    port=3306
)


"""def crearUsuario(nombres,correo,clave):
    cursor=usuario.cursor()
    cursor.execute('''insert into usuarios(nombre,email,contrasena) 
    values(%s,%s,%s)''',(nombres,correo,clave,))
    usuario.commit()
    cursor.close()"""
    

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
                contracena=input("crea una contraceña: ")
                if len(contracena)>=8:
                    mayusculas=[]
                    cont=0
                    aux=0
                    for contra in contracena:
                        mayusculas.append(contra)
                while aux<len(contracena):
                
                 if contracena[aux]==(mayusculas[aux]).upper:
                     
                  print(mayusculas[aux])
                  
                  aux=len(contracena);
                  
                print(mayusculas[aux])              
                if len(contracena)<8:
                    print("Contraseña demaciado corta")
                    
                    
                
            if opc==2:
                correo=input("ingresa tu correo: ")
                contraceña=input("ingrese su contraceña: ")
                  
                
        