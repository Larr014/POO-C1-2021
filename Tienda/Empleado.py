from Persona import *
class Empleado(Persona): #Empleado hereda de Persona -> Un empleado es una Persona

    def __init__(self): #Recibo parametros para crear un empleado
        super().__init__() #Llamo al constructor de la super clase para crear la Persona -> Cargar los atributos que lo hacen persona
        self.__sueldo = float(input("Ingrese sueldo: "))
        self.__salud = input("Ingrese salud: ")
        self.__afp = input("Ingrese afp: ")


    def mostrar(self): #Sobrescribiendo el metodo mostrar que esta en Persona
        super().mostrar() #Llama al metodo mostrar de la super clase -> La clase Persona
        print(f'Sueldo: {self.__sueldo}')
        print(f'Salud: {self.__salud}')
        print(f'AFP: {self.__afp}')
        
    def calcular_salario_neto(self):
        descuento_salud = self.__sueldo * 0.07
        descuento_afp = self.__sueldo * 0.1
        sueldo_neto = self.__sueldo - descuento_afp - descuento_salud
        print(f'Sueldo Bruto: {self.__sueldo}')
        print(f'Descuento Salud: {descuento_salud}')
        print(f'Descuento AFP: {descuento_afp}')
        print(f'Sueldo Neto: {sueldo_neto}')