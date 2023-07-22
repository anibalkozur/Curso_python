from tkinter import *

raiz=Tk()
raiz.iconbitmap("C:/Users/Aniba/OneDrive/Escritorio/estudio programacion/Curso_python/Graficos/linian logo cuadrado.ico")

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

#cuadroTexto=Entry(miFrame)
#cuadroTexto.place(x=100, y=100)

#nombreLabel=Label(miFrame, text="Nombre:")
#nombreLabel.place(x=100, y=100)

#mejor que place() es mejor el metodo grid()
#row - filas
#colums - columnas

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg="red", justify="left")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1)

#, sticky="e" posiciona el texto con respecto a los ejes cardinales
#pady - padx -distancia del objeto a los limites del contenedor
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

passLabel=Label(miFrame, text="password:")
passLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)


apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion de casa:")
direccionLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)


raiz.mainloop()
