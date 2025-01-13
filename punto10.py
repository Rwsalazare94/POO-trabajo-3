import tkinter as tk
from tkinter import messagebox

class CalculoPago:
    def __init__(self, patrimonio, estrato):
        self.patrimonio = patrimonio
        self.estrato = estrato
        self.matricula = 50000

    def pagoMatricula(self):
        if self.patrimonio > 2000000 and self.estrato > 3:
            self.matricula = self.matricula + (0.03 * self.patrimonio)
        return self.matricula


class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Universidad")

        # Crear los widgets
        self.jLabel1 = tk.Label(root, text="Universidad", font=("Segoe UI", 24))
        self.jLabel1.grid(row=0, column=0, columnspan=2, pady=10)

        self.jLabel2 = tk.Label(root, text="Nombres:")
        self.jLabel2.grid(row=1, column=0)

        self.jLabel3 = tk.Label(root, text="Numero de Inscripción:")
        self.jLabel3.grid(row=2, column=0)

        self.jLabel4 = tk.Label(root, text="Estrato Social:")
        self.jLabel4.grid(row=3, column=0)

        self.jLabel5 = tk.Label(root, text="Patrimonio:")
        self.jLabel5.grid(row=4, column=0)

        self.jLabel6 = tk.Label(root, text="Nombres:")
        self.jLabel6.grid(row=5, column=0)

        self.jLabel7 = tk.Label(root, text="Numero de Inscripción:")
        self.jLabel7.grid(row=6, column=0)

        self.jLabel9 = tk.Label(root, text="Pago de Matrícula:")
        self.jLabel9.grid(row=7, column=0)

        self.txtNI1 = tk.Entry(root)
        self.txtNI1.grid(row=2, column=1)

        self.txtNombres = tk.Entry(root)
        self.txtNombres.grid(row=1, column=1)

        self.txtPatrimonio = tk.Entry(root)
        self.txtPatrimonio.grid(row=4, column=1)

        self.txtEstrato = tk.Entry(root)
        self.txtEstrato.grid(row=3, column=1)

        self.txtNI2 = tk.Entry(root)
        self.txtNI2.grid(row=6, column=1)
        self.txtNI2.config(state=tk.DISABLED)

        self.txtNombres2 = tk.Entry(root)
        self.txtNombres2.grid(row=5, column=1)
        self.txtNombres2.config(state=tk.DISABLED)

        self.txtPago = tk.Entry(root)
        self.txtPago.grid(row=7, column=1)
        self.txtPago.config(state=tk.DISABLED)

        self.calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular.grid(row=8, column=0, columnspan=2, pady=10)

        self.borrar = tk.Button(root, text="Borrar", command=self.borrar)
        self.borrar.grid(row=9, column=0, columnspan=2)

        self.salir = tk.Button(root, text="Salir", command=root.quit)
        self.salir.grid(row=10, column=0, columnspan=2)

    def calcular(self):
        try:
            ni = self.txtNI1.get()
            nombres = self.txtNombres.get()
            patrimonio = float(self.txtPatrimonio.get())
            estrato = float(self.txtEstrato.get())

            # Crear la instancia de la clase de cálculo
            calculo = CalculoPago(patrimonio, estrato)
            pago = calculo.pagoMatricula()

            # Mostrar los resultados
            self.txtNI2.config(state=tk.NORMAL)
            self.txtNI2.delete(0, tk.END)
            self.txtNI2.insert(0, ni)

            self.txtNombres2.config(state=tk.NORMAL)
            self.txtNombres2.delete(0, tk.END)
            self.txtNombres2.insert(0, nombres)

            self.txtPago.config(state=tk.NORMAL)
            self.txtPago.delete(0, tk.END)
            self.txtPago.insert(0, f"${pago:,.2f}")

            # Deshabilitar los campos de resultado
            self.txtNI2.config(state=tk.DISABLED)
            self.txtNombres2.config(state=tk.DISABLED)
            self.txtPago.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos.")

    def borrar(self):
        self.txtNI1.delete(0, tk.END)
        self.txtNombres.delete(0, tk.END)
        self.txtPatrimonio.delete(0, tk.END)
        self.txtEstrato.delete(0, tk.END)
        self.txtNI2.config(state=tk.NORMAL)
        self.txtNI2.delete(0, tk.END)
        self.txtNombres2.config(state=tk.NORMAL)
        self.txtNombres2.delete(0, tk.END)
        self.txtPago.config(state=tk.NORMAL)
        self.txtPago.delete(0, tk.END)
        self.txtNI2.config(state=tk.DISABLED)
        self.txtNombres2.config(state=tk.DISABLED)
        self.txtPago.config(state=tk.DISABLED)


# Crear la ventana principal
root = tk.Tk()

# Crear la interfaz
interfaz = Interfaz(root)

# Ejecutar la aplicación
root.mainloop()
