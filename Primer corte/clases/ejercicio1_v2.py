

'''
palabra=str(input("ingrese una palabra: "))



if palabra.count("a")>0:
    print("letra a", palabra.count("a"))

if palabra.count("b")>0:
    print("letra b", palabra.count("b"))

if palabra.count("c")>0:
    print("letra c", palabra.count("c"))

if palabra.count("d")>0:
    print("letra d", palabra.count("d"))

if palabra.count("e")>0:
    print("letra e", palabra.count("e"))

if palabra.count("f")>0:
    print("letra f", palabra.count("f"))

if palabra.count("g")>0:
    print("letra g", palabra.count("g"))

if palabra.count("h")>0:
    print("letra h", palabra.count("h"))

if palabra.count("i")>0:
    print("letra i", palabra.count("i"))

if palabra.count("j")>0:
    print("letra j", palabra.count("j"))

if palabra.count("k")>0:
    print("letra k", palabra.count("k"))

if palabra.count("l")>0:
    print("letra l", palabra.count("l"))

if palabra.count("m")>0:
    print("letra m", palabra.count("m"))

if palabra.count("n")>0:
    print("letra n", palabra.count("n"))

if palabra.count("o")>0:
    print("letra o", palabra.count("o"))

if palabra.count("p")>0:
    print("letra p", palabra.count("p"))

if palabra.count("q")>0:
    print("letra q", palabra.count("q"))


if palabra.count("s")>0:
    print("letra s", palabra.count("s"))


if palabra.count("r")>0:
    print("letra r", palabra.count("r"))

 
if palabra.count("t")>0:
    print("letra t", palabra.count("t"))

if palabra.count("u")>0:
    print("letra u", palabra.count("u"))   

if palabra.count("v")>0:
    print("letra v", palabra.count("v"))   

if palabra.count("w")>0:
    print("letra w", palabra.count("w"))  

if palabra.count("x")>0:
    print("letra x", palabra.count("x"))  

if palabra.count("y")>0:
    print("letra y", palabra.count("y")) 

if palabra.count("z")>0:
    print("letra z", palabra.count("z"))       
'''

texto ="esta lloviendo"

'''resultado={

}

for letra in texto:
  
    if resultado.get(letra):
        resultado[letra]+=1
    else:
         resultado[letra]=1

print(resultado)'''

letrasUnicas=[]
for letra in texto:
    cont=0
    for letraUnica in letrasUnicas:
        if letraunica == letra:
            cont+=1

        if cont==0:
            letrasUnicas.append(letra)

for letraUnica in letrasUnicas:
    print(letraUnica,texto.count(letraUnica))


