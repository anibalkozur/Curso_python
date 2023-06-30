#continue, ignora esa vuelta del bucle y salta a la siguiente
#pass, devuelve null, no ejecuta el bucle
#else, es lo mismo que en un codicional if, for

for letra in "python":
    if letra=="h":
        continue#ignora la letra h
    print("Viendo las letras de python: "+ letra)


nombre="anibal kozur"
for i in nombre:
    if i==" ":#ignora en el conteo de caracateres el espacio
        continue
    contador=+1
print("la cantidad de letras de anibal kozur es: "+ str(len(nombre)))



class MiClase:
    pass # para implementar mas tarde devuelve un null


email=input("introduce email: ")
for i in email:
    if i=="@":
        arroba=True
        break;
else:#entra despues de que termine completamente el bucle for, si for no se completa no entra al else
    arroba=False
print("The email is " + str(arroba))