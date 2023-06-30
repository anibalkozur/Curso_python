print("Programa de becas año 2023")
distancia_escuela=int(input("introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("introduce el n° de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar=int(input("introduce salario anual bruto: "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 and salario_familiar<=20000:
    print("tienes derecho a beca")
else:
    print("no tienes derecho a beca")
