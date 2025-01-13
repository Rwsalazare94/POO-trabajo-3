import tkinter as tk
from tkinter import messagebox
import math

class TrianguloApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Triángulo")
        
        # Etiquetas
        self.label_titulo = tk.Label(root, text="Triángulo", font=("Segoe UI", 36), anchor="center")
        self.label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        self.label_lado = tk.Label(root, text="Lado")
        self.label_lado.grid(row=1, column=0, padx=10, pady=5)

        self.label_area = tk.Label(root, text="Área")
        self.label_area.grid(row=2, column=0, padx=10, pady=5)

        self.label_perimetro = tk.Label(root, text="Perímetro")
        self.label_perimetro.grid(row=3, column=0, padx=10, pady=5)

        self.label_altura = tk.Label(root, text="Altura")
        self.label_altura.grid(row=4, column=0, padx=10, pady=5)

        # Campos de entrada
        self.txt_lado = tk.Entry(root)
        self.txt_lado.grid(row=1, column=1, padx=10, pady=5)

        self.txt_area = tk.Entry(root, state="readonly")
        self.txt_area.grid(row=2, column=1, padx=10, pady=5)

        self.txt_perimetro = tk.Entry(root, state="readonly")
        self.txt_perimetro.grid(row=3, column=1, padx=10, pady=5)

        self.txt_altura = tk.Entry(root, state="readonly")
        self.txt_altura.grid(row=4, column=1, padx=10, pady=5)

        # Botones
        self.btn_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.btn_calcular.grid(row=5, column=0, padx=10, pady=20)

        self.btn_borrar = tk.Button(root, text="Borrar", command=self.borrar)
        self.btn_borrar.grid(row=5, column=1, padx=10, pady=20)

        self.btn_salir = tk.Button(root, text="Salir", command=root.quit)
        self.btn_salir.grid(row=5, column=2, padx=10, pady=20)

    def calcular(self):
        try:
            lado = float(self.txt_lado.get())
            if lado <= 0:
                raise ValueError("El lado debe ser un número positivo")

            # Crear instancia de la clase Triangulo y realizar cálculos
            triangulo = Triangulo(lado)

            # Obtener área, perímetro y altura
            area = triangulo.area()
            perimetro = triangulo.perimetro()
            altura = triangulo.altura()

            # Mostrar resultados
            self.txt_area.config(state="normal")
            self.txt_area.delete(0, tk.END)
            self.txt_area.insert(0, f"{area:.2f}")
            self.txt_area.config(state="readonly")

            self.txt_perimetro.config(state="normal")
            self.txt_perimetro.delete(0, tk.END)
            self.txt_perimetro.insert(0, f"{perimetro:.2f}")
            self.txt_perimetro.config(state="readonly")

            self.txt_altura.config(state="normal")
            self.txt_altura.delete(0, tk.END)
            self.txt_altura.insert(0, f"{altura:.2f}")
            self.txt_altura.config(state="readonly")

        except ValueError as e:
            messagebox.showerror("Error", f"Error de entrada: {e}")

    def borrar(self):
        self.txt_lado.delete(0, tk.END)
        self.txt_area.config(state="normal")
        self.txt_area.delete(0, tk.END)
        self.txt_area.config(state="readonly")
        self.txt_perimetro.config(state="normal")
        self.txt_perimetro.delete(0, tk.END)
        self.txt_perimetro.config(state="readonly")
        self.txt_altura.config(state="normal")
        self.txt_altura.delete(0, tk.END)
        self.txt_altura.config(state="readonly")

class Triangulo:
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        # Fórmula para el área de un triángulo equilátero: (lado^2 * √3) / 4
        return (self.lado ** 2 * math.sqrt(3)) / 4

    def perimetro(self):
        # Fórmula para el perímetro de un triángulo equilátero: 3 * lado
        return 3 * self.lado

    def altura(self):
        # Fórmula para la altura de un triángulo equilátero: (√3 / 2) * lado
        return (math.sqrt(3) / 2) * self.lado

if __name__ == "__main__":
    root = tk.Tk()
    app = TrianguloApp(root)
    root.mainloop()
