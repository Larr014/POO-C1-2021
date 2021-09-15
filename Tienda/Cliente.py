from Persona import *
class Cliente(Persona):

    def __init__(self):
        super().__init__()
        self.__telefono = input("Ingrese telefono: ")

    def mostrar(self):
        super().mostrar() #Muestro los atributos de la clase super -> Persona
        print(f'Telefono: {self.__telefono}')