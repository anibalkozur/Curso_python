from tkinter import *

raiz=Tk()
miFrame=Frame()
miFrame.pack()


#---------------pantalla----------------------
pantalla=Entry(miFrame)
pantalla.grid(row=1, column=1, padx=10, pady=10)
pantalla.config(background="black", fg="#03f943", justify="right")

#--------------fila 1--------------------


raiz.mainloop()