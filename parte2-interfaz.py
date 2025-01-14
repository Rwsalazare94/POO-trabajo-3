import tkinter as tk
from tkinter import Toplevel

class InterfazCirculo(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Círculo")
        self.geometry("300x200")
        label = tk.Label(self, text="Calculadora de Círculo", font=("Segoe UI", 18))
        label.pack(pady=20)

        # Aquí agregas los widgets para la calculadora del círculo
        # Ejemplo: Radio, Área, Circunferencia

        btn_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        btn_cerrar.pack(pady=20)

class InterfazRectangulo(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Rectángulo")
        self.geometry("300x200")
        label = tk.Label(self, text="Calculadora de Rectángulo", font=("Segoe UI", 18))
        label.pack(pady=20)

        # Aquí agregas los widgets para la calculadora del rectángulo
        # Ejemplo: Base, Altura, Área, Perímetro

        btn_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        btn_cerrar.pack(pady=20)

class InterfazCuadrado(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cuadrado")
        self.geometry("300x200")
        label = tk.Label(self, text="Calculadora de Cuadrado", font=("Segoe UI", 18))
        label.pack(pady=20)

        # Aquí agregas los widgets para la calculadora del cuadrado
        # Ejemplo: Lado, Área, Perímetro

        btn_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        btn_cerrar.pack(pady=20)

class InterfazTriangulo(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Triángulo")
        self.geometry("300x200")
        label = tk.Label(self, text="Calculadora de Triángulo", font=("Segoe UI", 18))
        label.pack(pady=20)

        # Aquí agregas los widgets para la calculadora del triángulo
        # Ejemplo: Base, Altura, Área, Perímetro, Hipotenusa

        btn_cerrar = tk.Button(self, text="Cerrar", command=self.destroy)
        btn_cerrar.pack(pady=20)

class InterfazPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("400x400")

        # Etiqueta de título
        label = tk.Label(self, text="Figuras Geométricas", font=("Segoe UI", 18))
        label.pack(pady=20)

        # Botones para las distintas figuras geométricas
        self.rectangulo_btn = tk.Button(self, text="Rectángulo", width=20, height=2, command=self.abrir_rectangulo)
        self.rectangulo_btn.pack(pady=10)

        self.circulo_btn = tk.Button(self, text="Círculo", width=20, height=2, command=self.abrir_circulo)
        self.circulo_btn.pack(pady=10)

        self.triangulo_btn = tk.Button(self, text="Triángulo", width=20, height=2, command=self.abrir_triangulo)
        self.triangulo_btn.pack(pady=10)

        self.cuadrado_btn = tk.Button(self, text="Cuadrado", width=20, height=2, command=self.abrir_cuadrado)
        self.cuadrado_btn.pack(pady=10)

        # Botón para salir
        self.salir_btn = tk.Button(self, text="Salir", width=20, height=2, command=self.salir)
        self.salir_btn.pack(pady=20)

    def abrir_rectangulo(self):
        InterfazRectangulo(self)

    def abrir_circulo(self):
        InterfazCirculo(self)

    def abrir_triangulo(self):
        InterfazTriangulo(self)

    def abrir_cuadrado(self):
        InterfazCuadrado(self)

    def salir(self):
        self.quit()

if __name__ == "__main__":
    app = InterfazPrincipal()
    app.mainloop()
