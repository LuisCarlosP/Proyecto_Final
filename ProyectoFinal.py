import tkinter as tk
from tkinter import messagebox
import sympy as sp


def menu():
    print("Menu de Formulas Notables:")
    print("1. Cuadrado de un binomio (a + b)^2")
    print("2. Producto de binomios con término común (a + b)(c + b)")
    print("3. Cubo de un binomio (a + b)^3")


def cuadrado_binomio(expr):
    return sp.expand(expr**2)


def producto_binomios_termino_comun(expr1, expr2):
    return sp.expand(expr1 * expr2)


def cubo_binomio(expr):
    return sp.expand(expr**3)


def calcular(choice, expr1=None, expr2=None):
    expr1 = expr1.replace('^', '**') if expr1 else None
    expr2 = expr2.replace('^', '**') if expr2 else None
   
    if choice == 1:
        try:
            expr = sp.sympify(expr1.replace('(', '').replace(')', ''))
            result = cuadrado_binomio(expr)
            result_str = str(result).replace('**', '^')
            messagebox.showinfo("Resultado", f"({expr})^2 = {result_str}")
        except:
            messagebox.showerror("Error", "Expresión inválida. Intente nuevamente.")
   
    elif choice == 2:
        try:
            expr1 = sp.sympify(expr1.replace('(', '').replace(')', ''))
            expr2 = sp.sympify(expr2.replace('(', '').replace(')', ''))
            result = producto_binomios_termino_comun(expr1, expr2)
            result_str = str(result).replace('**', '^')
            messagebox.showinfo("Resultado", f"({expr1})({expr2}) = {result_str}")
        except:
            messagebox.showerror("Error", "Expresión inválida. Intente nuevamente.")
   
    elif choice == 3:
        try:
            expr = sp.sympify(expr1.replace('(', '').replace(')', ''))
            result = cubo_binomio(expr)
            result_str = str(result).replace('**', '^')
            messagebox.showinfo("Resultado", f"({expr})^3 = {result_str}")
        except:
            messagebox.showerror("Error", "Expresión inválida. Intente nuevamente.")


def main():
    ventana = tk.Tk()
    ventana.title("Calculadora de Fórmulas Notables")
   
    def seleccionar_formula():
        choice = opcion.get()
       
        if choice == 1 or choice == 3:
            etiqueta_expr1.config(text="Expresión:")
            etiqueta_expr2.pack_forget()
            entrada_expr2.pack_forget()
        elif choice == 2:
            etiqueta_expr1.config(text="Primer binomio:")
            etiqueta_expr2.config(text="Segundo binomio:")
            etiqueta_expr2.pack()
            entrada_expr2.pack()
        boton_calcular.pack_forget()
        boton_calcular.pack(pady=20)
   
    def calcular_resultado():
        choice = opcion.get()
        expr1 = entrada_expr1.get()
        expr2 = entrada_expr2.get() if opcion.get() == 2 else None
        calcular(choice, expr1, expr2)


    opcion = tk.IntVar()
    opcion.set(1)


    etiqueta_menu = tk.Label(ventana, text="Seleccione una fórmula:", font=("Arial", 12))
    etiqueta_menu.pack(pady=10)


    menu1 = tk.Radiobutton(ventana, text="Cuadrado de un binomio (a + b)^2", variable=opcion, value=1, command=seleccionar_formula, font=("Arial", 10))
    menu1.pack(anchor=tk.CENTER)


    menu2 = tk.Radiobutton(ventana, text="Producto de binomios con término común (a + b)(c + b)", variable=opcion, value=2, command=seleccionar_formula, font=("Arial", 10))
    menu2.pack(anchor=tk.CENTER)


    menu3 = tk.Radiobutton(ventana, text="Cubo de un binomio (a + b)^3", variable=opcion, value=3, command=seleccionar_formula, font=("Arial", 10))
    menu3.pack(anchor=tk.CENTER)


    etiqueta_expr1 = tk.Label(ventana, text="Expresión:", font=("Arial", 10))
    etiqueta_expr1.pack(pady=5)


    entrada_expr1 = tk.Entry(ventana, width=30, font=("Arial", 10))
    entrada_expr1.pack(pady=5)


    etiqueta_expr2 = tk.Label(ventana, text="Segundo binomio:", font=("Arial", 10))


    entrada_expr2 = tk.Entry(ventana, width=30, font=("Arial", 10))


    boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_resultado, font=("Arial", 12), bg="blue", fg="white")
    boton_calcular.pack(pady=20)


    ventana.mainloop()


if __name__ == "__main__":
    main()