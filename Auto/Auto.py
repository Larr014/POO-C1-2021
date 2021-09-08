class Auto:
    ruedas = 4 #Las variables de clase son compartidas

    def __init__(self,color,aceleracion):
        self.color = color #El color es una variable del objeto
        self.aceleracion = aceleracion #La aceleracion es una variable del objeto
        self.velocidad = 0 #La velocidad es una variable del objeto

    def avanzar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):
        v = self.velocidad - self.aceleracion
        if v<0:
            v=0
        self.velocidad = v