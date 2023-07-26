from tkinter import *
#hay que importar messagebox para ventanas emergentes
from tkinter import messagebox

root=Tk()

#funcion para la ventana emergente
def infoAdicional():
    messagebox.showinfo("Empresa Linian", "Empresa creada en 2020 por Ian Kozur")

def avisoLicencia():
    messagebox.showwarning("Licencia", "Derechos reservados a Linian 2020")

def salirAplicacion():
    #salir=messagebox.askquestion("Salir", "¿Desea salir realmente?")
    salir=messagebox.askokcancel("Salir", "¿Desea salir realmente?")
    #if salir=="yes":
    if salir==True:
        root.destroy()

def cerrarDocumento():
    salir=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento cerrado")
    if salir==False:
        root.destroy()   

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

#con tearoff=0 desaparecen las lineas de separacion del menu
archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_command(label="Salir", command=salirAplicacion)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoHerramientas=Menu(barraMenu, tearoff=0)

archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="ayuda", menu=archivoAyuda)


root.mainloop()