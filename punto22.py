import tkinter as tk
from tkinter import messagebox

class Respuesta:
    def __init__(self, horas_mes, valor_hora, nombre):
        self.horas_mes = horas_mes
        self.valor_hora = valor_hora
        self.nombre = nombre

    def comparacion(self):
        salario = self.horas_mes * self.valor_hora
        return f"{self.nombre}, tu salario mensual es: ${salario:,.2f}"


class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Cálculo de Salario")

        # Crear los widgets
        self.jLabel2 = tk.Label(root, text="Nombres:")
        self.jLabel2.grid(row=0, column=0, padx=10, pady=5)

        self.jLabel3 = tk.Label(root, text="Horas trabajadas al mes:")
        self.jLabel3.grid(row=1, column=0, padx=10, pady=5)

        self.jLabel4 = tk.Label(root, text="Valor de la hora:")
        self.jLabel4.grid(row=2, column=0, padx=10, pady=5)

        self.txtNombre = tk.Entry(root)
        self.txtNombre.grid(row=0, column=1, padx=10, pady=5)

        self.txtHorasMes = tk.Entry(root)
        self.txtHorasMes.grid(row=1, column=1, padx=10, pady=5)

        self.txtValorHora = tk.Entry(root)
        self.txtValorHora.grid(row=2, column=1, padx=10, pady=5)

        self.txtRespuesta = tk.Entry(root)
        self.txtRespuesta.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
        self.txtRespuesta.config(state=tk.DISABLED)

        self.calcular = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular.grid(row=4, column=0, padx=10, pady=5)

        self.borrar = tk.Button(root, text="Borrar", command=self.borrar)
        self.borrar.grid(row=4, column=1, padx=10, pady=5)

        self.salir = tk.Button(root, text="Salir", command=root.quit)
        self.salir.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    def calcular(self):
        try:
            nombre = self.txtNombre.get()
            horas_mes = float(self.txtHorasMes.get())
            valor_hora = float(self.txtValorHora.get())

            # Crear la instancia de la clase Respuesta
            respuesta = Respuesta(horas_mes, valor_hora, nombre)
            resp = respuesta.comparacion()

            # Mostrar la respuesta
            self.txtRespuesta.config(state=tk.NORMAL)
            self.txtRespuesta.delete(0, tk.END)
            self.txtRespuesta.insert(0, resp)
            self.txtRespuesta.config(state=tk.DISABLED)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos.")

    def borrar(self):
        self.txtNombre.delete(0, tk.END)
        self.txtHorasMes.delete(0, tk.END)
        self.txtValorHora.delete(0, tk.END)
        self.txtRespuesta.config(state=tk.NORMAL)
        self.txtRespuesta.delete(0, tk.END)
        self.txtRespuesta.config(state=tk.DISABLED)


# Crear la ventana principal
root = tk.Tk()

# Crear la interfaz
interfaz = Interfaz(root)

# Ejecutar la aplicación
root.mainloop()
