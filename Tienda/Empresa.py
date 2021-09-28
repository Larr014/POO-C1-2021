from Empleado import *
from Cliente import *
class Empresa:



    def __init__(self):
        self.__id = input('Ingrese id de la empresa: ')
        self.__nombre = input('Ingrese nombre de la empresa: ')
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
    
    def eliminar_cliente(self):
        #Necesito conocer el cliente
            rut = input("Ingrese rut del cliente a eliminar: ")
            for cliente in self.__clientes:
                if cliente.get_rut() == rut: #Comparo el rut de cada cliente con el rut ingresado por el usuario
                    #Sacarlo de la empresa
                    self.__clientes.remove(cliente) 

    def agregar_empleado(self):
        e = Empleado() #Creo el empleado dentro de la empresa
        self.__empleados.append(e)

    def mostrar_empleados(self):
        for empleado in self.__empleados:
            empleado.mostrar()

    def eliminar_empleado(self):
        self.mostrar_empleados()
        #Necesito conocer el cliente
        rut = input("Ingrese rut del empleado a eliminar: ")
        for empleado in self.__empleados:
            if empleado.get_rut() == rut: #Comparo el rut de cada cliente con el rut ingresado por el usuario
            #Sacarlo de la empresa
                self.__empleados.remove(empleado) 

    def mostrar(self):
        print(f"Nombre: {self.__nombre}")

    def get_id(self):
        return self.__id

    

        
