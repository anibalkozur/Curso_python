def divide():
    try:
        op1=float(input("introduce el primer numero: "))
        op2=(float(input("introduce el segundo numero: ")))
        print("La division es: " + str(op1/op2))
    except ValueError:#se encadenan excepciones de forma consecutivas
        print("el valor introducido es erroneo")
    except ZeroDivisionError:
        print("no se puede dividir entre cero")
    finally:#lo que esta dentro de finally se va a ejecutar siempre
    #se puede sacar las excepciones pero el finally se ejecuta igual    
        print("Calculo finalizado")
    #except: sin valor es generico a todas las excepciones
    #no hay que poner una a una cada excepcion
    #pero no se puede especificar al usuario el tipo de error
    
divide()