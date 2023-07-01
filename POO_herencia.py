#gerarquia de herencia
#1-Clase padre superclase
#2-Subclase
#3-Clases

#sirve para la reutilizacion del codigo
#en caso de objetos similares
#con caracteristicas comunes y
#comportamientos en comun

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
        
class Moto(Vehiculos):
    pass

miMoto=Moto("Honda", "CBR")

miMoto.estado()