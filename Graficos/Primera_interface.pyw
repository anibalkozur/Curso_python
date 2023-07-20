from tkinter import *

#se cra un objeto ventana
raiz=Tk()

raiz.title("Ventana de Ian")
#cambiar el icono
raiz.iconbitmap("C:/Users/Aniba/OneDrive/Escritorio/estudio programacion/Curso_python/Graficos/linian logo cuadrado.ico")
#bloquea el tamaño de ventana (width "ancho", height "alto")
#raiz.resizable(1,0)#true-false

raiz.geometry("650x350")

raiz.config(bg="blue")

#es necesario para que se visualice la ventana en un bucle infinito
raiz.mainloop()

#para que funcione la ventana sin la consola
#se cambia la extencion .py por pyw