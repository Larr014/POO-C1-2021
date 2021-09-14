class Figura:

    def __init__(self,lado=0,longitud=0.0,apotema=0.0):
        self.lado = lado
        self.long = longitud
        self.__apotema=apotema
        self.__perimetro = self.lado * self.long

    def __area(self):
        resultado = (self.__apotema*self.__perimetro)/2
        return resultado

    def imprimir(self):
        print("-------")
        print(f'Lado: {self.lado}')
        print(f'Longitud: {self.long}')
        print(f'Apotema: {self.__apotema}')
        print(f'Perimetro: {self.__perimetro}')
        print(f'Area: {self.__area()}')
        print("-------")
        