class Coche():
    #propiedades del objeto
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False   
    #metodos(comportamiento)
    #(una funcion especial que pertenece a la clase)
    def arrancar(self):#(ser de)se pone el nombre que se quiera
    #self hace referencia al propio objeto perteneciente a la clase
    #hace referencia a la instancia perteneciente a la clase
    #cambia los valores de las propiedades
    #como no teine especificado que parametro le ingresa
    #por convencion se coloca self y dentro se especifica
    #las propiedades de aca no son cambiables como si las propiedades
        self.enmarcha=True     

    def estado(self):
        if(self.enmarcha):#igual a True(no hce falta colocar)
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

miCoche=Coche()#objeto o intancia-nombre de la clase a la que pertenece
#instanciar una clase, crear un ejemplar
print("el largo del coche es:",miCoche.largoChasis,"cm")
#para acceder nomenclatura del punto
print("El coche tiene:",miCoche.ruedas,"ruedas")
miCoche.arrancar()#hace una llamada al metodo arrancar
#recibe de parametro el propio objeto
#es como decir miCoche.enmarcha=True
print(miCoche.estado())

#falta ver: 
# estado inicial del objeto(con un contructor)
# encapsulacion