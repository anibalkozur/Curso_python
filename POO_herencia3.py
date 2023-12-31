#funciones
#super() and isinstance()

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

class Furgoneta(Vehiculos):
    def carga(self,cargar):
        self.cargado=cargar
        if(self.cargado):
            return "la furgoneta esta cargada"
        else:
            return "la furgoneta no esta cargada"

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
        
class VElectricos(Vehiculos):
    def __init__ (self, marca, modelo):

        super().__init__(marca, modelo)
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=(True)

miMoto=Moto("Honda", "CBR")
miMoto.caballito()#sobrescritura de metodos
#el segundo metodo sobreescribe el metodo padre
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

#se puere heredar de dos clases (herencia multple)
class BicicletaElectrica(VElectricos, Vehiculos):
    pass

#se da preferencia a la primera clase que se indique
#utiliza el metodo __init__ de VElectricos
#la funcion super() llama al metodo de la calse padre
miBici=BicicletaElectrica("obea", "maxi")