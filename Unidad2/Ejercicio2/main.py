from Persona import *
import crud

def registrar_persona():
    p = Persona()
    crud.registrar_persona(p)


def buscar_persona():
    pass

def modificar_persona():
    pass

def eliminar_persona():
    pass

def mostrar_personas():
    crud.mostrar_personas()


while True:
    print('1.- Registrar Persona')
    print('2.- Buscar Persona')
    print('3.- Modificar Persona')
    print('4.- Eliminar Persona')
    print('5.- Mostrar Personas')
    opcion = input("Ingrese una opcion: ")
    if opcion == '1':
        registrar_persona()
    elif opcion == '2':
        buscar_persona()
    elif opcion == '3':
        modificar_persona()
    elif opcion == '4':
        eliminar_persona()
    elif opcion == '5':
        mostrar_personas()
    else:
        print("Opcion no valida!")