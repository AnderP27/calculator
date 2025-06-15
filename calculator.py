import tkinter as tk
from tkinter import messagebox

def suma():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        resultado = num1 + num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "¡Ingresa solo números!")

def resta():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        resultado = num1 - num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
               messagebox.showerror("Error", "¡Ingresa solo números!")

def multiplicacion():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        resultado = num1 * num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
               messagebox.showerror("Error", "¡Ingresa solo números!")

def division():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        resultado = num1 / num2
        etiqueta_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
               messagebox.showerror("Error", "¡Ingresa solo números!")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora Basica")
ventana.geometry("300x300")

# Entradas de texto
tk.Label(ventana, text="Número 1:").pack()
entrada_num1 = tk.Entry(ventana)
entrada_num1.pack()

tk.Label(ventana, text="Número 2:").pack()
entrada_num2 = tk.Entry(ventana)
entrada_num2.pack()

# Botón para sumar
boton_sumar = tk.Button(ventana, text="Sumar", command=suma)
boton_sumar.pack(pady=10)

# Botón para restar
boton_restar = tk.Button(ventana, text="Restar", command=resta)
boton_restar.pack(pady=10)

# Botón para multiplicar
boton_restar = tk.Button(ventana, text="Multiplicar", command=multiplicacion)
boton_restar.pack(pady=10)

# Botón para dividir
boton_restar = tk.Button(ventana, text="Dividir", command=division)
boton_restar.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.pack()

ventana.mainloop()