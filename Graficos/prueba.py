from tkinter import *
from PIL import Image, ImageTk

ruta_imagen = "C:/Users/Aniba/OneDrive/Escritorio/estudio programacion/Curso_python/Graficos/linian logo cuadrado.png"
imagen = Image.open(ruta_imagen)

# Obtener el modo de color de la imagen
modo_color = imagen.mode
print(f"La imagen tiene {modo_color} canales.")

root = Tk()
root.iconbitmap("C:/Users/Aniba/OneDrive/Escritorio/estudio programacion/Curso_python/Graficos/linian logo cuadrado.ico")

# el frame creado está en la raíz root
miFrame = Frame(root, width=500, height=400)
# Evita que el Frame se ajuste al contenido dentro de él
miFrame.pack_propagate(False)
miFrame.pack()

# Convertir la imagen de PIL a PhotoImage de Tkinter
miImagen = ImageTk.PhotoImage(imagen)

Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()
