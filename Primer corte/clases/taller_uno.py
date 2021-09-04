
def suma(numero,numero1):
    if numero1<0:
         return -suma(numero,-numero1)
    if numero1==0:
        return 0
    elif numero1==1:
        return numero
    else:
        return numero+suma(numero,numero1-1)



cadena=input("ingrese multiplicacion,ulice el signo *")
numeros=[]
cont=0
while cont<=len(cadena):
      if cadena[cont]=="*":
          numeros.append(signo-1)
          print(numeros)
 cont+=1
      




