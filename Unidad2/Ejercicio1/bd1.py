import mysql.connector #Que vamos a usar mysql

#Declarar credenciales de acceso a la base de datos
credenciales = {'host':'localhost', #El host -> localhost
    'user':'root',
    'password':'',
    'database':'bd1'
}

#Establecer conexion con esas credenciales
conexion = mysql.connector.connect(**credenciales)

#Cuando quiero recuperar datos de una tabla, necesito un cursor
cursor = conexion.cursor()

#Crear una query
query = "SELECT * FROM people" #Busca todo desde la tabla people

#Cursor ejecuta esa query
cursor.execute(query)

#Cursor retorna el resultado
resultados = cursor.fetchall() #Si me retorna muchos

print(resultados)
print()

for tupla in resultados:
    print(f'{tupla[0]} {tupla[1]} {tupla[7]}')