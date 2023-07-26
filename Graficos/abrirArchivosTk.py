from tkinter import *
from tkinter import filedialog


root=Tk()

def abreFichero():
    #devuelve la ruta del archivo a abrir, se puede especificar donde, y tambien que tipos de archivos
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="c:", filetypes=(("Ficheros de Pytho","*.py"),("Ficheros de tecto","*.txt"),("Todos","*.*")))
    print(fichero)


Button (root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()