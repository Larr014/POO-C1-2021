from Empleado import *
class Empresa:



    def __init__(self,nombre):
        self.__nombre = nombre
        self.__empleados = [] #Una empresa tiene una lista de empleados
        self.__clientes = [] #Una empresa tiene una lista de clientes

    def agregar_empleado(self):
        e = Empleado() #Creamos un empleado 
        self.__empleados.append(e) #Agregamos a la lista

    def mostrar_empleados(self):
        for e in self.__empleados: #Por cada empleado de la lista
            e.mostrar() #Muestrame sus datos
    

