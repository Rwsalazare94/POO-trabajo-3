import tkinter as tk
from tkinter import messagebox


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class InterfazRectangulo:
    def __init__(self, root):
        self.root = root
        self.root.title("Rectángulo")

        # Labels
        tk.Label(root, text="Rectángulo", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(root, text="Base:").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        tk.Label(root, text="Altura:").grid(row=2, column=0, pady=5, padx=5, sticky="e")
        tk.Label(root, text="Área:").grid(row=3, column=0, pady=5, padx=5, sticky="e")
        tk.Label(root, text="Perímetro:").grid(row=4, column=0, pady=5, padx=5, sticky="e")

        # Entry fields
        self.txt_base = tk.Entry(root)
        self.txt_altura = tk.Entry(root)
        self.txt_area = tk.Entry(root, state="readonly")
        self.txt_perimetro = tk.Entry(root, state="readonly")

        self.txt_base.grid(row=1, column=1, pady=5, padx=5)
        self.txt_altura.grid(row=2, column=1, pady=5, padx=5)
        self.txt_area.grid(row=3, column=1, pady=5, padx=5)
        self.txt_perimetro.grid(row=4, column=1, pady=5, padx=5)

        # Buttons
        tk.Button(root, text="Calcular", command=self.calcular).grid(row=5, column=0, pady=10, padx=5)
        tk.Button(root, text="Limpiar", command=self.limpiar).grid(row=5, column=1, pady=10, padx=5)
        tk.Button(root, text="Salir", command=self.salir).grid(row=6, column=0, columnspan=2, pady=5)

    def calcular(self):
        try:
            base = float(self.txt_base.get())
            altura = float(self.txt_altura.get())

            rect = Rectangulo(base, altura)
            area = rect.calcular_area()
            perimetro = rect.calcular_perimetro()

            self.txt_area.config(state="normal")
            self.txt_perimetro.config(state="normal")

            self.txt_area.delete(0, tk.END)
            self.txt_perimetro.delete(0, tk.END)

            self.txt_area.insert(0, f"{area:.2f}")
            self.txt_perimetro.insert(0, f"{perimetro:.2f}")

            self.txt_area.config(state="readonly")
            self.txt_perimetro.config(state="readonly")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def limpiar(self):
        self.txt_base.delete(0, tk.END)
        self.txt_altura.delete(0, tk.END)

        self.txt_area.config(state="normal")
        self.txt_perimetro.config(state="normal")
        self.txt_area.delete(0, tk.END)
        self.txt_perimetro.delete(0, tk.END)
        self.txt_area.config(state="readonly")
        self.txt_perimetro.config(state="readonly")

    def salir(self):
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazRectangulo(root)
    root.mainloop()
