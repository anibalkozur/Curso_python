#esctructuras extraen valores de una funcion
#se almacenan en objetos iterables, se pueden recorrer con bulces while, for, metodo next
#se almacena de uno en uno

#yield
#es mas eficiente al devolver valores de uno en uno
#menos espacio de memoria
#utilidad de listas de valores infinitos

#sin generador
def generaPares(limite):
    num=1
    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num=num+1
    return miLista

print(generaPares(10))

#con generador
#entre llamda y llamada y entra en suspension cada ves que se lo llame
def generaParesyield(limite):
    numero=1
    while numero<limite:
        yield numero*2
        numero=numero+1
devuelvePares=generaParesyield(10)
for i in devuelvePares:
    print(i)
