for i in ["Clarita","Ian","Francesca", "Cintia"]: #recorre 3 veces la lista e imprime "hola 3 veces"
    print("hola", end=" ")#con end no hace salto de linea
    print(i)#imprime uno a uno cada objeto de la lista

for j in "anibal":
    print("letras", end=" ")#imprime tantas "letras como letras tiene el str del for"
print("")

email=False
email_ingresado = input("introduzca email: ")
for a in email_ingresado:#recorre letra por letra el email
    if a=="@":#verifica si contiene @
        email=True#si hay @ pone la variable en verdadero
if email:# simplifica el poner email==True:
    print("email es correcto")
else:
    print("el email no es correcto")

for x in range(5):#crea una lista de 5 elementos
    print(x)

for z in range(5,50,3):#crea una lista de elementos, desde el 5 hasta el 50 de tres en tres
    print(f"valor de la variable: {z}")#funcion de tipo f donde une textos con varables

print (len("anibalito"))#da la longitud de caracteres del str

valido=False
otroemail=input("introduce otro email: ")
for h in range(len(otroemail)):
    if otroemail[h]=="@":
        valido=True
if valido:
    print("otro email es correcto")
else:
    print("otro email es incorrecto")

