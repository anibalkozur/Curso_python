#simplifica el codigo de los generadores en el caso de utilizar bucles anidados
def devuelve_ciudades(*ciudades):#*recibe un numero indeterminado de argumentos en forma de tupla
    for elemento in ciudades:#recorre los elementos recibidos
        #for subElemento in elemento:#devuelve las letras de cada elemento
            yield from elemento#devuelve las letras de a uno desde cada elemento
#llama a la funsion y le pasa agumentos
ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao","Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))#imprime de a una las letras del primer elemento
