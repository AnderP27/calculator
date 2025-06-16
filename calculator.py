import tkinter as tk
from tkinter import messagebox

# Funciones de operaciones básicas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

# Diccionario 
operaciones = {
    '+': suma,
    '-': resta,
    '*': multiplicacion,
    '/': division
}

# Función principal que maneja el cálculo
def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        operador = operador_var.get()
        
        if operador in operaciones:
            resultado = operaciones[operador](num1, num2)
            etiqueta_resultado.config(text=f"Resultado: {resultado:.3f}")  # 3 decimales
        else:
            messagebox.showerror("Error", "Operación no válida")
    except ValueError:
        messagebox.showerror("Error", "¡Ingresa solo números!")
    except ZeroDivisionError:
        messagebox.showerror("Error", "No se puede dividir por cero")

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora Basica")
ventana.geometry("700x400")

# Entradas de texto
tk.Label(ventana, text="Número 1:").grid(row=0, column=0)
entrada_num1 = tk.Entry(ventana)
entrada_num1.grid(row=0, column=1)

tk.Label(ventana, text="Número 2:").grid(row=1, column=0)
entrada_num2 = tk.Entry(ventana)
entrada_num2.grid(row=1, column=1)

# Selector de operación
tk.Label(ventana, text="Operación:").grid(row=2, column=0)
operador_var = tk.StringVar(ventana)
operador_var.set('+')  # valor por defecto
operador_menu = tk.OptionMenu(ventana, operador_var, *operaciones.keys())
operador_menu.grid(row=2, column=1)

# Botón de cálculo
tk.Button(ventana, text="Calcular", command=calcular).grid(row=3, columnspan=2)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.grid(row=4, columnspan=2)

ventana.mainloop()