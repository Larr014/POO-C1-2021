import mysql.connector
from Persona import *
credenciales = {
    'host':'localhost',
    'user':'root',
    'password':'',
    'database':'bd1'
}

conexion = mysql.connector.connect(**credenciales)
cursor = conexion.cursor()

def registrar_persona(persona):
    query = "INSERT INTO people (fullname,profession,birth,genre,bodyweight,height,nationality) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (persona.get_fullname(),persona.get_profession(),persona.get_birth(),persona.get_genre(),persona.get_bodyweight(),persona.get_height(),persona.get_nationality())
    #Cursor ejecute la query con esos valores
    cursor.execute(query,val)
    #Despues de ejecutar un insert la base de datos debe hacer commit(aplicar cambios)
    conexion.commit()
    
def mostrar_personas():
    query = "SELECT * FROM people"
    cursor.execute(query)
    resultados = cursor.fetchall()
    for tupla in resultados:
        print(tupla)