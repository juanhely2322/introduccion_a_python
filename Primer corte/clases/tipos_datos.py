
"""
int
float
str
list=> array mutable
tupl=>array no mutable
dict=>objetos

"""
numero1=10#int
numero2=10.5 #float
nombre="juan"#str





#lista o array=>[]
materias=["base de datos ","lenguage 4 generacion","matematicas"]
listaNumeros=[1,2,3,4,5,7]
matriz=[[1,2],[3,4]]

materias[0]="programacion avansada"
print(materias[0])
print(matriz[0][0])
print(materias[1], materias[2])
print(matriz)

listaSinOrdenar=[10,20,35,-5,-1,34]
print(listaSinOrdenar)
#.sort(reverse=False) ordenar de menor a mayor
listaSinOrdenar.sort(reverse=False)
print(listaSinOrdenar)
#.sort(reverse=True) ordenar de mayor a menor
listaSinOrdenar.sort(reverse=True)
print(listaSinOrdenar)


#tuplas
dias=("lunes","martes","miercoles","jueves","viernes","sabado","domingo","lunes")
#esto no se puede hacer en una tupla ejemplo dias[3]="jhjd"
print(dias[3])
print(dias.count("lunes"))#contar ocurriencia o repeticiones
print(len(dias))#contar cantidad de objetos

#diccionario=> lleva llaves{}

persona={
    'nombre': "juan",
    "apellido" : "puentes",
    "edad": 12,
    "materias_persona":["algebra","ingles","español"],

    "direccion":{
        "direcion":"barrio centro",
        "ciudad":"mocoa",
        "pais":"colombia"
    }

}

persona["apellido"]="zarate"
print(persona["apellido"])

print(persona["materias_persona"][2])

print(persona["direccion"]["pais"])

persona["nombre_completo"]=persona["nombre"]+" "+persona["apellido"]
print(persona)





#ciclo for
for materia in materias:
    print("este codigo pertenece al cilo")
    print(materia)
print("este codigo no pertece al cliclo")

#operadores aritmeticos +,-,*,/,% ptencia **


#operadores relacionales <>=>=<=  !=


if 10>20:
    print("correcto")
elif 5<21:
    print("se cumple el elif")    
elif 55>21:
        print("se cumple el elif2")  
else:
    print("incorrecto")  

#input capturardatos en consola
print("cual es tu nombre")

nombre=input()
print("bienvenido ",nombre)

apellido=str(input("ingresa tu apellido "))
print(apellido)


    

