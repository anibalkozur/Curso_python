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

#minombre= cadena de caracteres
minombre=StringVar()
#el cuadroNobre esta asociado con el valor de minombre
cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg="red", justify="left")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

textComentarios = Text(miFrame, width=16, height=5)
textComentarios.grid(row=4, column=1, pady=10)
scrollYComentarios= Scrollbar(miFrame, command=textComentarios.yview)
scrollYComentarios.grid(row=4, column=1, pady=10, sticky="nse")
textComentarios.config(yscrollcommand=scrollYComentarios.set)
#textoComentario=Text(miFrame, width=16, height=5)
#textoComentario.grid(row=4, column=1, padx=10, pady=10)
#creamos un objeto Scollbar que funciona de manera vertical
#scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
#scrollVert.grid(row=4, column=2)

#, sticky="e" posiciona el texto con respecto a los ejes cardinales
#pady - padx -distancia del objeto a los limites del contenedor
nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)

passLabel=Label(miFrame, text="password:")
passLabel.grid(row=1, column=0, sticky="w", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="w", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3, column=0, sticky="w", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="w", padx=10, pady=10)

#.set establece un valor a una variable
def codigoBoton():
    minombre.set("Anibal")

botonEnvio=Button(raiz, text="enviar", command=codigoBoton)
botonEnvio.pack()



raiz.mainloop()