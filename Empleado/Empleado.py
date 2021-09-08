class Empleado:

    def __init__(self):
        self.nombre = input("Ingrese nombre: ") 
        self.sueldo = float(input("Ingrese sueldo: "))

    def imprimir(self):
        print(f'Nombre: {self.nombre}')
        print(f'Sueldo: {self.sueldo}')

    def paga_impuestos(self):
        if self.sueldo > 3000:
            print(f"{self.nombre} Paga impuestos")
        else:
            print(f"{self.nombre} No paga impuestos")