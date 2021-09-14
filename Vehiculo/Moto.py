from Vehiculo import *
class Moto(Vehiculo):

    def __init__(self):
        super().__init__("Moto")

    def num_ruedas(self):
        print("La Moto tiene 2 ruedas")