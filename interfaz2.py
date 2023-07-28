import tkinter as tk

def on_click_viajar():
    print("¡Has seleccionado la opción Viajar!")

def on_click_comer():
    print("¡Has seleccionado la opción Comer!")

def on_click_mapa():
    print("¡Has seleccionado la opción Mapa!")

# Crear la ventana principal
root = tk.Tk()
root.title("Food Travel App")

# Crear botones interactivos
btn_viajar = tk.Button(root, text="Viajar", command=on_click_viajar)
btn_viajar.pack()

btn_comer = tk.Button(root, text="Comer", command=on_click_comer)
btn_comer.pack()

btn_mapa = tk.Button(root, text="Mapa", command=on_click_mapa)
btn_mapa.pack()

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
