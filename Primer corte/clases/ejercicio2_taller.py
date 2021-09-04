
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
'''
git --version

iniciamos por primera vez
git init= iniacia  un proyecto de git en la carpeta actual
git status= estado actual del respositorio comparando la vercion anterior
git add . = agrega todos los cambios
git commit -m "iniciando repositoriso"=  documenta los cambios  que hacemos

git branch -M main= crea rama
git remote add origin https://github.com/juanhely2322/introduccion_a_python.git=todos los cambios se van a subir al repositorio remoto


git push -u origin main   
 
 proyecto ya creado  y hacer modificaciones

 gid add .
 git coomit -m  "mensaje para el commit
 git push

 git clone https:// github.com/jusn........= clona un repositorio
 


 '''