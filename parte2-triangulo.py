import tkinter as tk
from tkinter import messagebox
import math

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2
    
    def calcular_perimetro(self):
        hipotenusa = self.calcular_hipotenusa()
        return self.base + self.altura + hipotenusa
    
    def calcular_hipotenusa(self):
        return math.sqrt(self.base**2 + self.altura**2)

class InterfazTriangulo:
    def __init__(self, root):
        self.root = root
        self.root.title("Triángulo Rectángulo")
        
        # Etiquetas
        self.label1 = tk.Label(self.root, text="Triángulo", font=("Segoe UI", 24))
        self.label1.grid(row=0, column=1, pady=10)

        self.label5 = tk.Label(self.root, text="Base")
        self.label5.grid(row=1, column=0, padx=10, pady=5)
        
        self.label2 = tk.Label(self.root, text="Altura")
        self.label2.grid(row=2, column=0, padx=10, pady=5)
        
        self.label3 = tk.Label(self.root, text="Área")
        self.label3.grid(row=3, column=0, padx=10, pady=5)
        
        self.label4 = tk.Label(self.root, text="Perímetro")
        self.label4.grid(row=4, column=0, padx=10, pady=5)
        
        self.label6 = tk.Label(self.root, text="Hipotenusa")
        self.label6.grid(row=5, column=0, padx=10, pady=5)

        # Entradas
        self.txtBase = tk.Entry(self.root)
        self.txtBase.grid(row=1, column=1, padx=10, pady=5)

        self.txtAltura = tk.Entry(self.root)
        self.txtAltura.grid(row=2, column=1, padx=10, pady=5)

        self.txtArea = tk.Entry(self.root, state="readonly")
        self.txtArea.grid(row=3, column=1, padx=10, pady=5)

        self.txtPerimetro = tk.Entry(self.root, state="readonly")
        self.txtPerimetro.grid(row=4, column=1, padx=10, pady=5)

        self.txtHipotenusa = tk.Entry(self.root, state="readonly")
        self.txtHipotenusa.grid(row=5, column=1, padx=10, pady=5)

        # Botones
        self.botonCalcular = tk.Button(self.root, text="Calcular", command=self.calcular)
        self.botonCalcular.grid(row=6, column=0, padx=10, pady=5)

        self.botonLimpiar = tk.Button(self.root, text="Limpiar", command=self.limpiar)
        self.botonLimpiar.grid(row=6, column=1, padx=10, pady=5)

        self.botonSalir = tk.Button(self.root, text="Salir", command=self.salir)
        self.botonSalir.grid(row=6, column=2, padx=10, pady=5)

    def calcular(self):
        try:
            base = float(self.txtBase.get())
            altura = float(self.txtAltura.get())
            
            triangulo = TrianguloRectangulo(base, altura)
            
            area = triangulo.calcular_area()
            perimetro = triangulo.calcular_perimetro()
            hipotenusa = triangulo.calcular_hipotenusa()
            
            self.txtArea.config(state="normal")
            self.txtPerimetro.config(state="normal")
            self.txtHipotenusa.config(state="normal")
            
            self.txtArea.delete(0, tk.END)
            self.txtPerimetro.delete(0, tk.END)
            self.txtHipotenusa.delete(0, tk.END)
            
            self.txtArea.insert(0, f"{area:.2f}")
            self.txtPerimetro.insert(0, f"{perimetro:.2f}")
            self.txtHipotenusa.insert(0, f"{hipotenusa:.2f}")
            
            self.txtArea.config(state="readonly")
            self.txtPerimetro.config(state="readonly")
            self.txtHipotenusa.config(state="readonly")
        
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

    def limpiar(self):
        self.txtBase.delete(0, tk.END)
        self.txtAltura.delete(0, tk.END)
        self.txtArea.config(state="normal")
        self.txtPerimetro.config(state="normal")
        self.txtHipotenusa.config(state="normal")
        
        self.txtArea.delete(0, tk.END)
        self.txtPerimetro.delete(0, tk.END)
        self.txtHipotenusa.delete(0, tk.END)
        
        self.txtArea.config(state="readonly")
        self.txtPerimetro.config(state="readonly")
        self.txtHipotenusa.config(state="readonly")

    def salir(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazTriangulo(root)
    root.mainloop()
