import tkinter as tk
from tkinter import messagebox

class FormularioP18:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulario P18")

        # Etiquetas
        self.label_nombre = tk.Label(root, text="Nombre")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=5)

        self.label_codigo = tk.Label(root, text="Codigo")
        self.label_codigo.grid(row=1, column=0, padx=10, pady=5)

        self.label_horas = tk.Label(root, text="Horas trabajadas")
        self.label_horas.grid(row=2, column=0, padx=10, pady=5)

        self.label_valor = tk.Label(root, text="Valor por hora")
        self.label_valor.grid(row=3, column=0, padx=10, pady=5)

        self.label_rete = tk.Label(root, text="Retefuente")
        self.label_rete.grid(row=4, column=0, padx=10, pady=5)

        self.label_salario_bruto = tk.Label(root, text="Salario bruto")
        self.label_salario_bruto.grid(row=5, column=0, padx=10, pady=5)

        self.label_salario_neto = tk.Label(root, text="Salario neto")
        self.label_salario_neto.grid(row=6, column=0, padx=10, pady=5)

        # Campos de entrada
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=5)

        self.entry_codigo = tk.Entry(root)
        self.entry_codigo.grid(row=1, column=1, padx=10, pady=5)

        self.entry_horas = tk.Entry(root)
        self.entry_horas.grid(row=2, column=1, padx=10, pady=5)

        self.entry_valor = tk.Entry(root)
        self.entry_valor.grid(row=3, column=1, padx=10, pady=5)

        self.entry_rete = tk.Entry(root)
        self.entry_rete.grid(row=4, column=1, padx=10, pady=5)

        self.entry_salario_bruto = tk.Entry(root, state='readonly')
        self.entry_salario_bruto.grid(row=5, column=1, padx=10, pady=5)

        self.entry_salario_neto = tk.Entry(root, state='readonly')
        self.entry_salario_neto.grid(row=6, column=1, padx=10, pady=5)

        # Botones
        self.btn_calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.btn_calcular.grid(row=7, column=0, padx=10, pady=5)

        self.btn_borrar = tk.Button(root, text="Borrar", command=self.borrar)
        self.btn_borrar.grid(row=7, column=1, padx=10, pady=5)

        self.btn_salir = tk.Button(root, text="Salir", command=root.quit)
        self.btn_salir.grid(row=7, column=2, padx=10, pady=5)

    def calcular(self):
        try:
            # Obtener los valores de los campos de entrada
            horas = float(self.entry_horas.get())
            valor = float(self.entry_valor.get())
            rete = float(self.entry_rete.get()) / 100

            # Calcular salario bruto y neto
            salario_bruto = horas * valor
            descuento = salario_bruto * rete
            salario_neto = salario_bruto - descuento

            # Mostrar resultados
            self.entry_salario_bruto.config(state='normal')
            self.entry_salario_bruto.delete(0, tk.END)
            self.entry_salario_bruto.insert(0, f"{salario_bruto:.2f}")
            self.entry_salario_bruto.config(state='readonly')

            self.entry_salario_neto.config(state='normal')
            self.entry_salario_neto.delete(0, tk.END)
            self.entry_salario_neto.insert(0, f"{salario_neto:.2f}")
            self.entry_salario_neto.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores válidos.")

    def borrar(self):
        # Limpiar todos los campos
        self.entry_nombre.delete(0, tk.END)
        self.entry_codigo.delete(0, tk.END)
        self.entry_horas.delete(0, tk.END)
        self.entry_valor.delete(0, tk.END)
        self.entry_rete.delete(0, tk.END)
        self.entry_salario_bruto.config(state='normal')
        self.entry_salario_bruto.delete(0, tk.END)
        self.entry_salario_bruto.config(state='readonly')
        self.entry_salario_neto.config(state='normal')
        self.entry_salario_neto.delete(0, tk.END)
        self.entry_salario_neto.config(state='readonly')

if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioP18(root)
    root.mainloop()
