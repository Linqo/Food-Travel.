import tkinter as tk
from gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title("Food Travel")
    root.configure(bg="#FF5722")
    root.iconbitmap("img/foodlog.ico")
    #root.resizable(0,0)
    barra_menu(root)

    app = Frame(root = root)

    #frame = tk.Frame(root)
    #frame.pack()
    #frame.config(width = 480, height= 320, bg = "green")

    app.mainloop()

if __name__ == "__main__":
    main()    