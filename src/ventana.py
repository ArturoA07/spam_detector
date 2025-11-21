import tkinter as tk
from tkinter import messagebox

def mostar_mensaje():
    messagebox.showinfo("Boton precionado!")

ventana = tk.Tk()
ventana.title("Mi primera ventana")

label = tk.Label(ventana, text="Eso tilin!")
label.pack(pady=10)

boton = tk.Button(ventana, text="Click aqui!", command=mostar_mensaje)
boton.pack(pady=10)

ventana.mainloop()
