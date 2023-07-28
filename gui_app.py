import tkinter as tk
from data import DataJson

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width= 300, height= 300)

    menu_inicio = tk.Menu(barra_menu, tearoff = 0)
    barra_menu.add_cascade(label = "Inicio", menu = menu_inicio)

    menu_inicio.add_command(label = "Crear registro")
    menu_inicio.add_command(label = "Eliminar registro")
    menu_inicio.add_command(label = "Salir", command = root.destroy)

    barra_menu.add_cascade(label = "Mapa")
    barra_menu.add_cascade(label = "Espetaculos")
    barra_menu.add_cascade(label = "Planificacion")



class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width = 840, height= 720 )
        self.root = root
        self.pack()
        #self.config(bg = "#FF5722")

        self.campos_pelicula()

        self.ubicaciones()    

#Nombres
    def campos_pelicula(self):
        self.label_nombre = tk.Label(self, text = "Nombre")  
        self.label_nombre.config(font = ("Arial", 12, "bold")) 
        self.label_nombre.grid(row = 0, column = 0, padx = 10, pady = 10) 

        self.label_restaurant = tk.Label(self, text = "Restaurant")  
        self.label_restaurant.config(font = ("Arial", 12, "bold")) 
        self.label_restaurant.grid(row = 1, column = 0, padx = 10, pady = 10) 

        self.label_reseña = tk.Label(self, text = "Reseña")  
        self.label_reseña.config(font = ("Arial", 12, "bold")) 
        self.label_reseña.grid(row = 2, column = 0, padx = 10, pady = 10) 

#Entrys de cada campo
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width = 50, font=("Arial", 12) )
        self.entry_nombre.grid(row = 0, column = 1, padx=10, pady=10)

        self.entry_restaurant = tk.Entry(self)
        self.entry_restaurant.config(width = 50, state = "disable", font=("Arial", 12) )
        self.entry_restaurant.grid(row = 1, column = 1, padx=10, pady=10)

        self.entry_reseña = tk.Entry(self)
        self.entry_reseña.config(width = 50, state = "disable", font=("Arial", 12) )
        self.entry_reseña.grid(row = 2, column = 1, padx=10, pady=10)

    def ubicaciones (self):
        
        
        obj_json = DataJson('datos/ubicacion.json')    

        print(obj_json.leer_json())