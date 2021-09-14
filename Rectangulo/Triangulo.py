from Rectangulo import *
class Triangulo(Rectangulo):

    def __init__(self,base,altura):
        super().__init__(base,altura)

    def area(self):
        resultado = super().area()/2 #Usa el metodo area del rectangulo y lo divide en dos 
        return resultado
