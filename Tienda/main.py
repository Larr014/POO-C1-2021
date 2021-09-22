from Empleado import *
from Empresa import *
clientes = [] #Lista global de clientes
empresas = [] #Lista global de empresas

def agregar_empresa():
    nombre = input("Ingrese nombre de la empresa: ")
    empresa = Empresa(nombre) 
    empresas.append(empresa)

def mostrar_empresas():
    contador = 0
    print('----')
    for e in empresas:
        
        contador += 1
        print(f'{contador}',end=" ")
        e.mostrar()
    print('----')

def eliminar_empresa():
    mostrar_empresas()
    id = int(input("Ingrese id de la empresa a eliminar: "))
    empresas.pop(id-1)

  
#Ciclo infinito
while True:
    print('1.- Agregar Empresa')
    print('2.- Mostrar Empresas')
    print('3.- Eliminar Empresa')
    print('4.- Agregar Cliente')
    print('5.- Mostrar Clientes')
    print('6.- Eliminar Clientes')
    opcion = input("Ingrese una opcion: ")
    if opcion=="1":
        agregar_empresa()
    elif opcion=="2":
        mostrar_empresas()
    elif opcion=="3":
        eliminar_empresa()






