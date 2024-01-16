import tkinter as tk

def create_window():
    # Crear la ventana principal
    window = tk.Tk()
    window.title("Ta - Te - Ti")  # Establecer el título de la ventana

    # Etiqueta de bienvenida
    label = tk.Label(window, text="¡Bienvenido a Ta - Te - Ti!", font=("Arial", 18))
    label.grid(row=0, column=0, columnspan=3, pady=20)

    # Crear tablero 3x3 de cuadrados
    cuadrados = {}
    turno = "rojo"

    def click_cuadrado(i, j):
        nonlocal turno
        if cuadrados.get((i, j)) is None:
            color = "red" if turno == "rojo" else "blue"
            cuadrados[(i, j)] = color
            turno = "azul" if turno == "rojo" else "rojo"
            draw_circle(i, j, color)
            verificar_ganador(color)

    def draw_circle(i, j, color):
        square = tk.Frame(window, width=80, height=80, bd=2, relief=tk.RAISED)
        square.grid(row=i+1, column=j, padx=2, pady=2)
        circle = tk.Canvas(square, width=80, height=80, bg="white", highlightthickness=0)
        circle.pack()
        circle.create_oval(10, 10, 70, 70, fill=color)

    def verificar_ganador(color):
        for i in range(3):
            # Verificar filas
            if (cuadrados.get((i, 0)) == cuadrados.get((i, 1)) == cuadrados.get((i, 2)) == color):
                mostrar_ganador(color)
                return

            # Verificar columnas
            if (cuadrados.get((0, i)) == cuadrados.get((1, i)) == cuadrados.get((2, i)) == color):
                mostrar_ganador(color)
                return

        # Verificar diagonales
        if (cuadrados.get((0, 0)) == cuadrados.get((1, 1)) == cuadrados.get((2, 2)) == color):
            mostrar_ganador(color)
            return

        if (cuadrados.get((0, 2)) == cuadrados.get((1, 1)) == cuadrados.get((2, 0)) == color):
            mostrar_ganador(color)
            return

    def mostrar_ganador(color):
        ganador_label.config(text="¡Ganó el color {}!".format(color.capitalize()))
        ganador_label.grid(row=4, column=0, columnspan=3, pady=10)
        window.after(3000, reiniciar_tablero)

    def reiniciar_tablero():
        for (i, j) in cuadrados:
            cuadrados[(i, j)] = None
            square = tk.Frame(window, width=80, height=80, bd=2, relief=tk.RAISED)
            square.grid(row=i+1, column=j, padx=2, pady=2)
            square.bind("<Button-1>", lambda e, i=i, j=j: click_cuadrado(i, j))
            square.update()
        ganador_label.config(text="")
        ganador_label.grid_forget()

    ganador_label = tk.Label(window, text="", font=("Arial", 18))

    for i in range(3):
        for j in range(3):
            square = tk.Frame(window, width=80, height=80, bd=2, relief=tk.RAISED)
            square.grid(row=i+1, column=j, padx=2, pady=2)
            square.bind("<Button-1>", lambda e, i=i, j=j: click_cuadrado(i, j))

    # Mostrar la ventana
    window.mainloop()

if __name__ == "__main__":
    create_window()
