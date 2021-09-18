
def suma(numero,numero1):
    if numero1<0:
         return -suma(numero,-numero1)
    if numero1==0:
        return 0
    elif numero1==1:
        return numero
    else:
        return numero+suma(numero,numero1-1)



multiplicando=int(input("ingrese numero "))
multiplicador=int(input("ingrese numero "))
print(suma(multiplicando,multiplicador))
#comandos git 
