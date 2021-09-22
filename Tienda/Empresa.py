from Empleado import *
from Cliente import *
class Empresa:



    def __init__(self,nombre):
        self.__nombre = nombre
        self.__empleados = [] #Una empresa tiene una lista de empleados
        self.__clientes = [] #Una empresa tiene una lista de clientes

    '''Si es un rombo negro entre empleado y empresa, si empresa es el todo
        el empleado no puede existir si no existe la empresa 

        .- Debe crearse el empleado dentro de la empresa
    '''
    def agregar_empleado(self):
        e = Empleado() #Creamos un empleado 
        self.__empleados.append(e) #Agregamos a la lista

    def mostrar_empleados(self):
        for e in self.__empleados: #Por cada empleado de la lista
            e.mostrar() #Muestrame sus datos

    '''Si es un rombro blanco entre cliente y empresa, si empresa es el todo
    el cliente si puede existir si no existe la empresa
    
    .- Debe crearse el cliente fuera de la empresa'''
    def agregar_cliente(self,cliente):
        self.__clientes.append(cliente)

    def mostrar_clientes(self):
        for c in self.__clientes: #Por cada cliente de la lista
            c.mostrar() #Muestra sus datos
    
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        
