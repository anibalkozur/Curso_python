#String
#Metodos:

#upper(): convierte en mayusculas todas las letras de un String
#lower(): pasa a minuscula un String
#capitalize(): pone la primera letra en mayuscula
#count(): contar cuantas veces aparece una letra o cadena de caracateres
#find():posicion en la que aparece un caracter o cadena de caracteres
#isdigit(): devuelve un boleano si es numerico o no el valor
#isalum(): comprobar si es alfanumerico
#isalpha(): si hay solo letras, los espacios no cuentan
#split(): separa por palabras utilizando espacios
#strip(): borra los espacios sobrantes al principio y al final
#remplace(): cambia una un caracter o cadena por otra dentro del string
#rfind(): como find pero desde atras, posicion en la que aparece un caracter o cadena de caracteres

#hay mas
#nombreUsuario=input("introduce numero de usuario: ")

#print("El nombre es:", nombreUsuario)                    
#print("El nombre es:", nombreUsuario.upper())  
#print("El nombre es:", nombreUsuario.lower())  
#print("El nombre es:", nombreUsuario.capitalize()) 

#edad=input("Introduce la edad: ")
#print(edad.isdigit())#True-False

#ejemplo
edad=input("Introduce la edad: ")

while(edad.isdigit()==False):
    print("Por favor, introduce un valor numerico")
    edad=input("Introduce la edad: ")

if (int(edad)<18):
    print("No puede pasar")
else:
    print("No puede pasar")