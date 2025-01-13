import tkinter as tk
from tkinter import messagebox

class Comparacion:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def mayor(self):
        if self.a > self.b:
            return self.a
        else:
            return self.b
    
    def menor(self):
        if self.a < self.b:
            return self.a
        else:
            return self.b


class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Mayor o Menor")

        # Crear los widgets
        self.jLabel1 = tk.Label(root, text="Mayor o Menor", font=("Segoe UI", 24))
        self.jLabel1.grid(row=0, column=0, columnspan=2, pady=10)

        self.jLabel2 = tk.Label(root, text="Numero A:")
        self.jLabel2.grid(row=1, column=0)

        self.jLabel3 = tk.Label(root, text="Numero B:")
        self.jLabel3.grid(row=2, column=0)

        self.txtA = tk.Entry(root)
        self.txtA.grid(row=1, column=1)

        self.txtB = tk.Entry(root)
        self.txtB.grid(row=2, column=1)

        self.jLabel4 = tk.Label(root, text="El numero mayor es:")
        self.jLabel4.grid(row=3, column=0)

        self.txtMayor = tk.Entry(root)
        self.txtMayor.grid(row=3, column=1)
        self.txtMayor.config(state=tk.DISABLED)

        self.jLabel5 = tk.Label(root, text="El numero menor es:")
        self.jLabel5.grid(row=4, column=0)

        self.txtMenor = tk.Entry(root)
        self.txtMenor.grid(row=4, column=1)
        self.txtMenor.config(state=tk.DISABLED)

        self.calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular.grid(row=5, column=0, columnspan=3, pady=10)

        self.borrar = tk.Button(root, text="Borrar", command=self.borrar)
        self.borrar.grid(row=6, column=0, columnspan=3)

        self.salir = tk.Button(root, text="Salir", command=root.quit)
        self.salir.grid(row=7, column=0, columnspan=3)

    def calcular(self):
        try:
            a = float(self.txtA.get())
            b = float(self.txtB.get())

            comparacion = Comparacion(a, b)

            mayor = comparacion.mayor()
            menor = comparacion.menor()

            # Mostrar resultados
            self.txtMayor.config(state=tk.NORMAL)
            self.txtMayor.delete(0, tk.END)
            self.txtMayor.insert(0, mayor)

            self.txtMenor.config(state=tk.NORMAL)
            self.txtMenor.delete(0, tk.END)
            self.txtMenor.insert(0, menor)

            self.txtMayor.config(state=tk.DISABLED)
            self.txtMenor.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos.")

    def borrar(self):
        self.txtA.delete(0, tk.END)
        self.txtB.delete(0, tk.END)
        self.txtMayor.config(state=tk.NORMAL)
        self.txtMayor.delete(0, tk.END)
        self.txtMayor.config(state=tk.DISABLED)
        self.txtMenor.config(state=tk.NORMAL)
        self.txtMenor.delete(0, tk.END)
        self.txtMenor.config(state=tk.DISABLED)


# Crear la ventana principal
root = tk.Tk()

# Crear la interfaz
interfaz = Interfaz(root)

# Ejecutar la aplicación
root.mainloop()
