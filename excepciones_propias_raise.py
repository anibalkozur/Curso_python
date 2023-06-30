def evaluaEdad(edad):

    if edad<0:#se imprime el error q se quiera bajo una condicion
        raise TypeError("no se permiten edades negativas")
#el hilo del programa no continua como lo hace try-except
    if edad<20:#cuando se cumple uno de los condicionales sale sin seguir evaluando
        return "eres muy joven"
    elif edad<40:
        return "eres joven"
    elif edad<65:
        return "eres maduro"
    elif edad<100:
        return "cuidate..."

print(evaluaEdad(15))# ejmplo -15


import math

def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)
    
op1=(int(input("Introduce un numero: ")))

try:#escepcion de raiz de numero negativo
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:#se lo puede dar un nombre a ese error
    print(ErrorDeNumeroNegativo)

print("programa terminado")