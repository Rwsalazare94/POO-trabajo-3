import tkinter as tk
from tkinter import messagebox
import math

# Clase para realizar los cálculos relacionados con el círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Clase para la interfaz gráfica
class InterfazCirculo:
    def __init__(self, root):
        self.root = root
        self.root.title("Círculo")
        
        # Crear los widgets
        self.jLabel1 = tk.Label(root, text="Círculo", font=("Segoe UI", 24))
        self.jLabel1.grid(row=0, column=0, columnspan=2, pady=20)

        self.jLabel2 = tk.Label(root, text="Radio:")
        self.jLabel2.grid(row=1, column=0, padx=10, pady=5)

        self.jLabel3 = tk.Label(root, text="Área:")
        self.jLabel3.grid(row=2, column=0, padx=10, pady=5)

        self.jLabel4 = tk.Label(root, text="Perímetro:")
        self.jLabel4.grid(row=3, column=0, padx=10, pady=5)

        self.txtRadio = tk.Entry(root)
        self.txtRadio.grid(row=1, column=1, padx=10, pady=5)

        self.txtArea = tk.Entry(root, state="disabled")
        self.txtArea.grid(row=2, column=1, padx=10, pady=5)

        self.txtPerimetro = tk.Entry(root, state="disabled")
        self.txtPerimetro.grid(row=3, column=1, padx=10, pady=5)

        # Botones
        self.calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular.grid(row=4, column=0, padx=10, pady=10)

        self.limpiar = tk.Button(root, text="Limpiar", command=self.limpiar)
        self.limpiar.grid(row=4, column=1, padx=10, pady=10)

        self.salir = tk.Button(root, text="Salir", command=root.quit)
        self.salir.grid(row=5, column=0, columnspan=2, pady=10)

    def calcular(self):
        try:
            radio = float(self.txtRadio.get())
            circ = Circulo(radio)
            area = circ.calcular_area()
            perimetro = circ.calcular_perimetro()

            # Mostrar los resultados
            self.txtArea.config(state=tk.NORMAL)
            self.txtPerimetro.config(state=tk.NORMAL)
            self.txtArea.delete(0, tk.END)
            self.txtArea.insert(0, str(area))
            self.txtPerimetro.delete(0, tk.END)
            self.txtPerimetro.insert(0, str(perimetro))
            self.txtArea.config(state=tk.DISABLED)
            self.txtPerimetro.config(state=tk.DISABLED)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido para el radio.")

    def limpiar(self):
        self.txtRadio.delete(0, tk.END)
        self.txtArea.config(state=tk.NORMAL)
        self.txtArea.delete(0, tk.END)
        self.txtArea.config(state=tk.DISABLED)
        self.txtPerimetro.config(state=tk.NORMAL)
        self.txtPerimetro.delete(0, tk.END)
        self.txtPerimetro.config(state=tk.DISABLED)

# Crear la ventana principal
root = tk.Tk()

# Crear la interfaz
interfaz = InterfazCirculo(root)

# Ejecutar la aplicación
root.mainloop()
