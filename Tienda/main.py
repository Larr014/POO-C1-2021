from Empleado import *
from Empresa import *
clientes = [] #Lista global de clientes
empresas = [] #Lista global de empresas

def agregar_empresa():
    nombre = input("Ingrese nombre de la empresa: ")
    empresa = Empresa(nombre) 
    empresas.append(empresa)

def mostrar_empresas():
    for empresa in empresas:
        empresa.mostrar()

def eliminar_empresa():
    mostrar_empresas()
    id = input("Ingrese id de la empresa a eliminar: ")
    for empresa in empresas:
        if empresa.get_id() == id:
            empresas.remove(empresa)

def agregar_cliente():
    c = Cliente() #Creo un cliente
    clientes.append(c) #Agregar cliente a la lista clientes

def mostrar_clientes():
    for cliente in clientes: #Por cada cliente en la lista clientes
        cliente.mostrar() #Mostrar sus datos

def eliminar_cliente():
    mostrar_clientes()
    rut = input("Ingrese rut del cliente a eliminar: ")
    for cliente in clientes:
        if cliente.get_rut() == rut: #Comparo el rut de cada cliente con el rut ingresado por el usuario
            clientes.remove(cliente) #Elimino de la lista de clientes el cliente que cumple con lo anterior


def asociar_cliente():
    #Necesito conocer la empresa
    mostrar_empresas()
    id = int(input("Ingrese id de la empresa: "))
    for empresa in empresas:
        if empresa.get_id() == id:
            #Necesito conocer el cliente
            rut = input("Ingrese rut del cliente a asociar: ")
            for cliente in clientes:
                if cliente.get_rut() == rut: #Comparo el rut de cada cliente con el rut ingresado por el usuario
                    #Los asocio
                    empresa.agregar_cliente(cliente) #La empresa debe asociar ese cliente

def mostrar_clientes_empresa():
    #Necesito conocer la empresa
    mostrar_empresas()
    id = int(input("Ingrese id de la empresa: "))
    for empresa in empresas:
        if empresa.get_id() == id:
            empresa.mostrar_clientes()

def eliminar_cliente_empresa():
    #Necesito conocer la empresa
    mostrar_empresas()
    id = int(input("Ingrese id de la empresa: "))
    for empresa in empresas:
        if empresa.get_id() == id:
            empresa.eliminar_cliente()

def agregar_empleado():
    #Necesito conocer la empresa
    mostrar_empresas()
    id = int(input("Ingrese id de la empresa: "))
    for empresa in empresas:
        if empresa.get_id() == id:
            empresa.agregar_empleado()

def mostrar_empleados_empresa():
    #Necesito conocer la empresa
    mostrar_empresas()
    id = int(input("Ingrese id de la empresa: "))
    for empresa in empresas:
        if empresa.get_id() == id:
            empresa.mostrar_empleados()

def eliminar_empleados_empresa():
    #Necesito conocer la empresa
    mostrar_empresas()
    id = int(input("Ingrese id de la empresa: "))
    for empresa in empresas:
        if empresa.get_id() == id:
            empresa.eliminar_empleado()

#Ciclo infinito
while True:
    print('1.- Agregar Empresa')
    print('2.- Mostrar Empresas')
    print('3.- Eliminar Empresa')
    print('4.- Agregar Cliente')
    print('5.- Mostrar Clientes')
    print('6.- Eliminar Clientes')
    print('7.- Asociar cliente a empresa')
    print('8.- Mostrar clientes x empresa')
    print('9.- Eliminar cliente x empresa')
    print('10.- Agregar Empleado x empresa')
    print('11.- Mostrar Empleado x empresa')
    print('12.- Eliminar Empleado x empresa')
    opcion = input("Ingrese una opcion: ")
    if opcion=="1":
        agregar_empresa()
    elif opcion=="2":
        mostrar_empresas()
    elif opcion=="3":
        eliminar_empresa()
    elif opcion == '4':
        agregar_cliente()
    elif opcion == '5':
        mostrar_clientes()
    elif opcion == '6':
        eliminar_cliente()
    elif opcion == '7':
        asociar_cliente()
    elif opcion == '8':
        mostrar_clientes_empresa()
    elif opcion == '9':
        eliminar_cliente_empresa()
    elif opcion == '10':
        agregar_empleado()
    elif opcion == '11':
        mostrar_empleados_empresa()
    elif opcion == '12':
        eliminar_empleados_empresa()




