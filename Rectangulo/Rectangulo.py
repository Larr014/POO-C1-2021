class Rectangulo:

    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def area(self):
        resultado = self.base * self.altura
        return resultado