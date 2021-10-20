from Persona import *
import crud

def registrar_persona():
    fullname = input("Ingrese nombre: ")
    profession = input("Ingrese profesion: ")
    birth = input("Ingrese fecha de nacimiento (Año-Mes-dia): ")
    genre = input("Ingrese genero (M/F): ")
    bodyweight = float(input("Ingrese peso: "))
    height = float(input("Ingrese altura: "))
    nationality = input("Ingrese nacionalidad: ")
    p = Persona(fullname,profession,birth,genre,bodyweight,height,nationality)
    crud.registrar_persona(p)


def buscar_persona():
    id = input("Ingrese id de la persona a buscar: ")
    crud.buscar_persona_id(id)


def modificar_persona():
    id = input("Ingrese id de la persona a modificar: ")
    #Buscar campos actuales de la persona
    tupla = crud.buscar_persona_id(id)
    #Creamos un objeto de la persona con sus campos actuales
    p = Persona(tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[6],tupla[7],id)

    #Preguntar por cada campo que el usuario quiera modificar
    #En caso que si quiera modificar, debemos hacer un set al campo que corresponda

    respuesta = input("Desea modificar el nombre: s/n ")
    if respuesta.lower() == 's':
        nombre = input("Ingrese nombre: ")
        p.set_fullname(nombre)
    respuesta = input("Desea modificar la profesion: s/n ")
    if respuesta.lower() == 's':
        profesion = input("Ingrese profesion: ")
    respuesta = input("Desea modificar fecha nacimiento: s/n ")
    if respuesta.lower() == 's':
        fecha = input("Ingrese fecha nacimiento: ")
    respuesta = input("Desea modificar genero: s/n ")
    if respuesta.lower() == 's':
        genero = input("Ingrese genero: M/F ")
    respuesta = input("Desea modificar el peso: s/n ")
    if respuesta.lower() == 's':
        peso = input("Ingrese peso: ")
    respuesta = input("Desea modificar la altura: s/n ")
    if respuesta.lower() == 's':
        altura = input("Ingrese altura: ")
    respuesta = input("Desea modificar la nacionalidad: s/n ")
    if respuesta.lower() == 's':
        nacionalidad = input("Ingrese nacionalidad: ")
    crud.modificar_persona(p)

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