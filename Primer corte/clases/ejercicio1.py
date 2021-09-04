
#crud para administrar contactos 
#1. crear un contact
#2leer un contacto
#3 actualizar un contacto
#4 borrar un contacto
#atributos nombres,apellidos,celular, correo electronico


def crearcontacto(nombre,apellido,celular,correo):
        contacto={

            "Nombre":nombre,
            "Apellido":apellido,
            "celular":celular,
            "correo":correo

        
        
        }


contacto=[]

print(  "               MENU")

print("1. Crear contacto")
print("2. ver contacto")
print("3. actualizar contacto")
print("4. borrar contacto")

opcion=input("elije una opcion")

if(opcion==1):

    nombre=str(input("ingrese nombre "))
    apellido=str(input("ingrese apellido"))
    celular=int(input("ingrese numero de celular"))
    correo=str(input("ingrese su correo "))
     contacto.append(crearcontacto(nombre,apellido,celular,correo))



    elif opcion==2:
        
         for contact in contacto:
             print(contact)


    elif(opcion==3):
    contace=str(input("ingrese nombre contacto a editar"))
       
    for persona in contacto:
        if(persona["Nombre"]==contace):
            
            crearcontacto()


