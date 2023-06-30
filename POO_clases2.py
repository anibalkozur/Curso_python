class Coche():
    #caracteristicas de estado inicial
    #se especifica con un constructor
    def __init__(self):#estado inicial
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4#queda encapsulado y no se puede cambiar
        self.__enmarcha=False   

    def arrancar(self,arrancamos):#recibe por parametro el propio objeto y 
        #se pasa un parametro
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"
        
    def estado(self):
        print("El coche tiene",self.__ruedas,"ruedas, un ancho de",
              self.__anchoChasis,"y un largo de",self.__largoChasis)

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("-------------A continuacion creamos el segundo objeto----------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.__ruedas=2#no cambia su valos.el programa no permite
#cambiar caracteristicas basicas de una propiedad
#se recurre a la encapsulacion con __antes del nombre
miCoche2.estado()


