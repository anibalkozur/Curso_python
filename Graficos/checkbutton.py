from tkinter import *

root = Tk()
root.title("Ejemplo")

playa=IntVar()
montagna=IntVar()
turismoRural=IntVar()

def opcionesViaje():

    opcionEscogida=""

    if(playa.get()==1):
        opcionEscogida+=" playa"

    if(montagna.get()==1):
        opcionEscogida+=" Montaña"

    if(turismoRural.get()==1):
        opcionEscogida+=" Turismo Rural"

    textoFinal.config(text=opcionEscogida)

foto = PhotoImage(file="Avion.png")

factor_escala = 6  # Factor de escala, 2 reducirá la imagen a la mitad (50%)

# Escalar la imagen con el método subsample
foto = foto.subsample(factor_escala, factor_escala)

Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montagna, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()
