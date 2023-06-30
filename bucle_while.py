i=1
while i<=10:
    print("paso "+ str(i)+" veces")
    i=i+1
print("termino de contar")

edad=int(input("introduce tu edad por favor: "))
while edad<5 or edad>120:
    print("has introducido una edad erronea, intentalo denuevo")
    edad=int(input("introduce tu edad por favor: "))
print("tu edad es: "+ str(edad) +" años")


import math # importa la calse math, matematica

print ("Programa de calculo de raiz cuadrada")
numero=int(input("Introduce un numero por favor: "))
intentos=0
while numero<0:
    print("No se puede hacer la raiz de un numero negativo")
    if intentos==2:
        print("has hecho demasiados intentos erroneos. Fin de programa")
        break;
    numero=int(input("introduce un numero por favor: "))
    if numero<0:
        intentos=intentos+1
    if intentos<2:
        solucion=math.sqrt(numero)
        print("La raiz cuadrada de " + str (numero) + " es " + str(solucion))
