import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print("Se ha creado una persona nueva con el nombre de", self.nombre)
#metodo especial str convierte en cadena de texto la informacion de un objeto
#para poder verlo y guardalo en u fichero externo
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
    
    personas=[]

    def __init__(self):
        #creamos una variable donde se guarda la creacion del fichero externo
        listadePersonas=open("ficheroExterno","ab+")#se crea fichero externo para grabar informacion binaria
        #se usa el metodo seek para desplazar el cursor al principio para poder leer el fichero
        #xq si queda al final, al tratar de leer el fichero, no leeria nada
        listadePersonas.seek(0)
        #esto es para leer la lista
        #try verifica si se puede realizar esta instruccion 
        #si hay personas cargadas en la lista
        try:
            self.personas=pickle.load(listadePersonas)
            #para visualizar, len de la lista de personas
            print("Se cargaron {} personas del fichero extero".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listadePersonas.close()
            del(listadePersonas)
        #se ejecuta si o si para cerrar la lista y borrarla

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonasEnFicheroExterno()

    def mostarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonasEnFicheroExterno(self):
        #se abre el archibo en modo de escritura
        ListaPersonas=open("ficheroExterno", "wb")
        #dump para el volcado de informacion de la lista de personas de los que tenemos almacenado de listapersonas
        pickle.dump(self.personas, ListaPersonas)
        ListaPersonas.close()
        del(ListaPersonas)

    def mostrarInfoFicheroExterno(self):
        print("La informacion del fichero externo es la siguiente")
        for p in self.personas:
            print(p)

miLista=ListaPersonas()

p=Persona("Cintia", "Femenino", 39)
miLista.agregarPersonas(p)
p=Persona("Francesca", "Femenino", 8)
miLista.agregarPersonas(p)
p=Persona("Anibal", "Masculino", 39)
miLista.agregarPersonas(p)
p=Persona("Ian", "Masculino", 10)
miLista.agregarPersonas(p)

miLista.mostarPersonas()

miLista.mostrarInfoFicheroExterno()
