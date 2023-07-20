from tkinter import *

#se cra un objeto ventana
raiz=Tk()

raiz.title("Ventana de Ian")
#cambiar el icono
raiz.iconbitmap("C:/Users/Aniba/OneDrive/Escritorio/estudio programacion/Curso_python/Graficos/linian logo cuadrado.ico")
#bloquea el tamaño de ventana (width "ancho", height "alto")
#raiz.resizable(1,0)#true-false

#raiz.geometry("650x350")
#la raiz siempre se adapta al frame inicialmente
raiz.config(bg="blue")

miFrame=Frame()
#hay que meterlo dentro de la raiz
#side="right"-queda pegado a la derecha
#side="bottom"-queda pegado abajo
#miFrame.pack(side="right", anchor="n")#anchor puntos cardinales

#rellena todo x al expandir la raiz
#para que rellene en y se agrega expand=true
#fill="both" para rellenar todo
miFrame.pack(fill="y", expand="True")

#configurar bordes
miFrame.config(bd=35)#bordes
miFrame.config(relief="raised")

#camibiar el cursor del frame
miFrame.config(cursor="pirate")

#para verlo
miFrame.config(bg="red")
#darle tamaño al frame
miFrame.config(width="650", height="350")


#es necesario para que se visualice la ventana en un bucle infinito
raiz.mainloop()

#para que funcione la ventana sin la consola
#se cambia la extencion .py por pyw