#Es un error en tiempo de ejecucion, no de sintaxis
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):	
	try:	
		return num1/num2
	except ZeroDivisionError:#genera una excepcion en la divicion por cero y continua el programa
		print("no se puede dividir por cero")
		return "operacion erronea"
while True:#bucle infinito mientras los valores ingresados no sean numeros
	try:	
		op1=(int(input("Introduce el primer número: ")))
		op2=(int(input("Introduce el segundo número: ")))
		break		
	except ValueError:#si los valores introducidos no son numeros
		print("Los valores introducidos no son correctos")
		print("Introduce nuevamente")

operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))
elif operacion=="resta":
	print(resta(op1,op2))
elif operacion=="multiplica":
	print(multiplica(op1,op2))
elif operacion=="divide":
	print(divide(op1,op2))
else:
	print ("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecución del programa ")