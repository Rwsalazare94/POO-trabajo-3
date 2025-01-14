import tkinter as tk
from tkinter import messagebox

# Clase para realizar los cálculos relacionados con el cuadrado
class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

# Clase para la interfaz gráfica
class InterfazCuadrado:
    def __init__(self, root):
        self.root = root
        self.root.title("Cuadrado")
        
        # Crear los widgets
        self.jLabel1 = tk.Label(root, text="Cuadrado", font=("Segoe UI", 24))
        self.jLabel1.grid(row=0, column=0, columnspan=2, pady=20)

        self.jLabel2 = tk.Label(root, text="Lado:")
        self.jLabel2.grid(row=1, column=0, padx=10, pady=5)

        self.jLabel3 = tk.Label(root, text="Área:")
        self.jLabel3.grid(row=2, column=0, padx=10, pady=5)

        self.jLabel4 = tk.Label(root, text="Perímetro:")
        self.jLabel4.grid(row=3, column=0, padx=10, pady=5)

        self.txtLado = tk.Entry(root)
        self.txtLado.grid(row=1, column=1, padx=10, pady=5)

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
            lado = float(self.txtLado.get())
            cuad = Cuadrado(lado)
            area = cuad.calcular_area()
            perimetro = cuad.calcular_perimetro()

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
            messagebox.showerror("Error", "Por favor ingrese un número válido para el lado.")

    def limpiar(self):
        self.txtLado.delete(0, tk.END)
        self.txtArea.config(state=tk.NORMAL)
        self.txtArea.delete(0, tk.END)
        self.txtArea.config(state=tk.DISABLED)
        self.txtPerimetro.config(state=tk.NORMAL)
        self.txtPerimetro.delete(0, tk.END)
        self.txtPerimetro.config(state=tk.DISABLED)

# Crear la ventana principal
root = tk.Tk()

# Crear la interfaz
interfaz = InterfazCuadrado(root)

# Ejecutar la aplicación
root.mainloop()
