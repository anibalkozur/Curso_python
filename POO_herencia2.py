#herencia sobre escritura de metodos
#herencia simple y multiple

class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print ("Marca:", self.marca, 
            "\nModelo:", self.modelo,
            "\nEn Marcha:" , self.enmarcha, 
            "\nAcelerando", self.acelera,
            "\nFrenando:", self.frena)#\n es un salto de linea

#heredamos el constructor y cuatro metodos        
class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):#mas otro metodo como comportamiento propio
        self.hcaballito="voy haciendo caballito"
    def estado(self):
        print ("Marca:", self.marca, 
            "\nModelo:", self.modelo,
            "\nEn Marcha:" , self.enmarcha, 
            "\nAcelerando", self.acelera,
            "\nFrenando:", self.frena,
            "\n", self.hcaballito)

miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()