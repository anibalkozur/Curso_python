#Poliformismo
#un objeto puede cambiar de forma y comportamiento

class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    
    def desplazamiento(self):
        print("Me desplazo untilizando seis ruedas")

#miVehiculo=Moto()
#miVehiculo.desplazamiento()

#miVehiculo2=Coche()
#miVehiculo2.desplazamiento()

#miVehiculo3=Camion()
#miVehiculo3.desplazamiento()

#se presinde de lo anterior y se hace
#poliformismo
def desplazamientoVehiculo(vehiculo):
    #llama al metodo desplazamiento de la clase camion
    vehiculo.desplazamiento()

miVehiculo4=Camion()

#llama a este metodo y se pasa el objeto miVehiculo4
desplazamientoVehiculo(miVehiculo4)

miVehiculo5=Coche()
desplazamientoVehiculo(miVehiculo5)

