#funciones
#super() and isinstance()

class Persona():

    def __init__(self, nombre, edad, Lugar_residencia):

        self.nombre=nombre
        self.edad=edad
        self.Lugar_residencia=Lugar_residencia

    def descripcion(self):
        print("nombre:", self.nombre, 
              "edad:", self.edad,
              "Residencia:", self.Lugar_residencia)
        
class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        #llama al metodo de la clase padre
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):

        super().descripcion()
        print("Salario:", self.salario, 
              "Antiguedad", self.antiguedad)

Manuel=Empleado(1500, 15, "Manuel", 55, "colombia")  
Manuel.descripcion()
#si un objeto es instancia de una clase determinada
#isintance() devuelve True-False
#print(isinstance(Manuel, Empleado))#da true
print(isinstance(Manuel, Persona))#da true tambien

Juan=Persona("juan", 25, "Brasil")
Juan.descripcion()
#print(isinstance(Juan, Persona))#devuelve True
print(isinstance(Juan, Empleado))#devuelve False