import tkinter as tk
from tkinter import messagebox

# Contador de veces que se muestra el menú
contador = 0
max_intentos = 6

# Funciones de los scripts
def ejecutar_script(nombre, funcion):
    global contador
    if contador < max_intentos:
        funcion()
        contador += 1
        if contador == max_intentos:
            messagebox.showinfo("Fin", "Se alcanzaron 6 ejecuciones. Cerrando el programa.")
            root.quit()  # Cierra la aplicación

def Supercias():
    messagebox.showinfo("Ejecutando", "Ejecutando Script Supercias...")

def SRI():
    messagebox.showinfo("Ejecutando", "Ejecutando Script SRI...")

def Iess():
    messagebox.showinfo("Ejecutando", "Ejecutando Script Iess...")

def Arcsa():
    messagebox.showinfo("Ejecutando", "Ejecutando Script Arcsa...")

def crear_ex():
    messagebox.showinfo("Ejecutando", "Creando Excel Final...")

# Crear ventana
root = tk.Tk()
root.title("Menú de Opciones")
root.geometry("300x300")

# Botones con contador de intentos
botones = [
    ("Ejecutar Script Supercias", Supercias),
    ("Ejecutar Script SRI", SRI),
    ("Ejecutar Script Iess", Iess),
    ("Ejecutar Script Arcsa", Arcsa),
    ("Crear Excel Final", crear_ex),
    ("Salir", root.quit)
]

for texto, funcion in botones:
    tk.Button(root, text=texto, command=lambda t=texto, f=funcion: ejecutar_script(t, f), width=30, height=2).pack(pady=5)

root.mainloop()
