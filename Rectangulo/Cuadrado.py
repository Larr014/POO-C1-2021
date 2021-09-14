from Rectangulo import *
class Cuadrado(Rectangulo): #Cuadrado hereda de Rectangulo

    def __init__(self,lado):
        super().__init__(lado,lado)

        