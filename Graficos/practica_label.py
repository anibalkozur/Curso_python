from tkinter import *

root=Tk()
root.iconbitmap("C:/Users/Aniba/OneDrive/Escritorio/estudio programacion/Curso_python/Graficos/linian logo cuadrado.ico")

#el frame creado esta en la raiz root
miFrame=Frame(root, width=500, height=400)
# Evita que el Frame se ajuste al contenido dentro de él
miFrame.pack_propagate(False)

miFrame.pack()

miImagen=PhotoImage(file="C:/Users/Aniba/OneDrive/Escritorio/estudio programacion/Curso_python/Graficos/linian logo cuadrado.png")

Label(miFrame, image=miImagen).place(x=100, y=200)

#miLabel= Label(miFrame, text="Hola a mis hijos, los amo con toda el alma", fg="red", font=("Brush Script MT Cursiva", 18))
#miLabel.place(x=100, y=200)





root.mainloop()