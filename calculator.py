import tkinter as tk
from tkinter import messagebox

"""# Funciones de operaciones básicas
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
"""
#Añade un número u operador a la pantalla
def agregar_numero(num):
    global operacion_actual
    operacion_actual += str(num)
    pantalla.delete(0, tk.END)
    pantalla.insert(0, operacion_actual)

#Funcion principal del calculo del resultado de la operación en pantalla
def calcular():
    global operacion_actual
    try:
        resultado = str(eval(operacion_actual))
        pantalla.delete(0, tk.END)
        pantalla.insert(0, resultado)
        operacion_actual = resultado
    except Exception as e:
        messagebox.showerror("ERROR", e)
        operacion_actual = ""
        pantalla.delete(0, tk.END)

#Limpia la pantalla completamente
def limpiar_pantalla():
    global operacion_actual
    operacion_actual = ""
    pantalla.delete(0, tk.END)

# Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora Basica")
ventana.geometry("320x400")

# Pantalla donde se verá la operación
pantalla = tk.Entry(ventana, font=('Arial', 20), justify='right', bd=10, insertwidth=2)
pantalla.grid(row=0, column=0, columnspan=4, pady=8)

# Variable para almacenar la operación
operacion_actual = ""

# Botones numéricos
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0)
]

for (texto, fila, col) in botones:
    boton = tk.Button(ventana, text=texto, padx=20, pady=20, font=('Arial', 14),
                     command=lambda t=texto: agregar_numero(t))
    boton.grid(row=fila, column=col)

# Botones de operaciones
operadores = [
    ('/', 1, 3), ('*', 2, 3),
    ('-', 3, 3), ('+', 4, 3),
    ('=', 4, 2), ('C', 4, 1)
]

for (texto, fila, col) in operadores:
    if texto == '=':
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, font=('Arial', 14),
                         command=calcular)
    elif texto == 'C':
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, font=('Arial', 14),
                         command=limpiar_pantalla)
    else:
        boton = tk.Button(ventana, text=texto, padx=20, pady=20, font=('Arial', 14),
                         command=lambda t=texto: agregar_numero(t))
    boton.grid(row=fila, column=col)

def test_exploit():
    from tkinter import simpledialog
    test_code = simpledialog.askstring("Modo Prueba", "Introduce código a evaluar:")
    try:
        eval(test_code)
        messagebox.showinfo("Resultado", "Codigo ejecutado")
    except Exception as e:
        messagebox.showerror("Error", str(e))

tk.Button(ventana, text="[MODO PRUEBA]", command=test_exploit, bg='red').grid(row=5, columnspan=4)

ventana.mainloop()