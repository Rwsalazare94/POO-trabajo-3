import tkinter as tk
from tkinter import messagebox
import math

# Clase para resolver la ecuación cuadrática
class Ecuaciones:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculo(self):
        disc = self.discriminante()
        
        if disc > 0:
            x1 = (-self.b + math.sqrt(disc)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(disc)) / (2 * self.a)
            return f"Las soluciones son: {x1} y {x2}"
        elif disc == 0:
            x = -self.b / (2 * self.a)
            return f"La solución es: {x}"
        else:
            return "No tiene soluciones reales"

    def discriminante(self):
        return (self.b ** 2) - (4 * self.a * self.c)

# Clase para la interfaz gráfica
class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Ecuación de Segundo Grado")
        
        # Crear los widgets
        self.jLabel1 = tk.Label(root, text="Ecuación de Segundo Grado", font=("Segoe UI", 18))
        self.jLabel1.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.jLabel2 = tk.Label(root, text="Término B:")
        self.jLabel2.grid(row=1, column=0, padx=10, pady=5)
        
        self.jLabel3 = tk.Label(root, text="Término A:")
        self.jLabel3.grid(row=2, column=0, padx=10, pady=5)
        
        self.jLabel4 = tk.Label(root, text="Término C:")
        self.jLabel4.grid(row=3, column=0, padx=10, pady=5)
        
        self.txtA = tk.Entry(root)
        self.txtA.grid(row=2, column=1, padx=10, pady=5)

        self.txtB = tk.Entry(root)
        self.txtB.grid(row=1, column=1, padx=10, pady=5)

        self.txtC = tk.Entry(root)
        self.txtC.grid(row=3, column=1, padx=10, pady=5)

        self.txtSlns = tk.Entry(root, state="disabled")
        self.txtSlns.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Botones
        self.calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular.grid(row=5, column=0, padx=10, pady=10)

        self.borrar = tk.Button(root, text="Borrar", command=self.borrar)
        self.borrar.grid(row=5, column=1, padx=10, pady=10)

        self.salir = tk.Button(root, text="Salir", command=root.quit)
        self.salir.grid(row=6, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            a = float(self.txtA.get())
            b = float(self.txtB.get())
            c = float(self.txtC.get())
            
            # Crear la instancia de la clase Ecuaciones
            solucion = Ecuaciones(a, b, c)
            respuesta = solucion.calculo()

            # Mostrar la respuesta
            self.txtSlns.config(state=tk.NORMAL)
            self.txtSlns.delete(0, tk.END)
            self.txtSlns.insert(0, respuesta)
            self.txtSlns.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")

    def borrar(self):
        self.txtA.delete(0, tk.END)
        self.txtB.delete(0, tk.END)
        self.txtC.delete(0, tk.END)
        self.txtSlns.config(state=tk.NORMAL)
        self.txtSlns.delete(0, tk.END)
        self.txtSlns.config(state=tk.DISABLED)

# Crear la ventana principal
root = tk.Tk()

# Crear la interfaz
interfaz = Interfaz(root)

# Ejecutar la aplicación
root.mainloop()
