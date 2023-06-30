print("asignaturas optativas año 2024")
print("asignaturas a elegir: informatica - matematica - fisica")
option=input("escribe la asignatura escogida: ")
asignatura=option.lower() 
#pone todas las letras en minusculas

if asignatura in ("informatica", "matematica", "fisica"):
#compara lo de asignatura con cada uno de los str del parentesis
    print("asignatura elegida: " + asignatura)
else:
    print("las asignatura escogida no esta contemplada")