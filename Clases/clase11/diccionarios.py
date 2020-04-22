#En los diccionarios podemos hacer uso del sistema llave valor.
#Esto indica que al igual que en un diccionarios real toda palabra tiene su significado.

#UN DICCIONARIO VACIO SE INDICA ASI:
#      diccionario = {}
#incluyendo su contenido

#EJEMPLO 1: FORMA 1
# Hagamos un diccionario de medios de transporte:
medios_transporte = {}
medios_transporte["carros"] = {"BMW", "AUDI", "MAZDA", "TOYOTA"}
medios_transporte["motos"] = {"AKT", "HONDA", "YAMAHA"}

print(medios_transporte)

#Tambien se pueden imprimir cada diccionario de manera individual:

print("Los elementos que componen la llave carros son : {}".format(medios_transporte["carros"]))

#En el caso de este diccionario podemos ver que se cuenta con dos llaves: carros y motos
#cuando se solicita la llave carro se devuelven los carros asociados a esta llave. Igualmente en el caso de las motos

print("Los elementos que componen la llave motos son : {}".format(medios_transporte["motos"]))

#ELEMPLO 2: FORMA 2
estudiantes_programacion = {"Nombres" : ["Daniel", "Valeria", "Santiago", "David", "Ysabella", "Maria Fernanda", "Elena"], "Edades": [20,18,19,21,19,18,19]}

print(estudiantes_programacion["Nombres"])

#Si queremos obtener solamente las llaves de ese diccionario; es decir, solo la especificacion del diccionario (carros, motos, nombres o edades),
# lo podemos hacer asi:

print(medios_transporte.keys()) 
print(estudiantes_programacion.keys())

#para poderlas iterar las transformamos en listas: (elimina el dict_keys que aparece al immprimir de la manera anterior)
print(list(medios_transporte.keys()))
print(list(estudiantes_programacion.keys()))

#Para obtener unicamente el contenido del diccionario:
print(medios_transporte.values())
print(estudiantes_programacion.values())

#para poderlas iterar las transformamos en lista:
print(list(medios_transporte.values()))
print(list(estudiantes_programacion.values()))

#si quiero ver la lista de valores en determinada posicion:
#en este caso me mostrara solo el primer conjunto de valores dentro de medios_transporte
valores = list(medios_transporte.values())
print(valores[0])

#LOS DICCIONARIOS NOS PERMITEN TENER DE UNA FORMA MAS ORGANIZADA LA INFORMACION.
#En ocasiones podemos ver diccionarios de diccionarios

#Ejemplo:
clases={}
clases["ESTUDIANTES"] = {"Laura", "Melissa", "Sofia"}
clases["PROFESORES"] = {"Diego", "Carolina"}
clases["AULAS"] = {"A202", "B1203"}

materiales={}
materiales["ORO"] = {"18k", "16k"}
materiales["MARCADORES"] = {"pelikan", "staedtler"}

clases["ELEMENTOS"] = materiales
print(clases["ELEMENTOS"]["MARCADORES"])
#LO QUE HICIMOS FUE METER EL DICCIONARIOS "MATERIALES", AHORA LLAMADO "ELEMENTOS" DENTRO DE "CLASES"

#Ejemplo:
notas = {}
notas["QUIZ1"] = {5,4,5,5,4,3,5}
notas["QUIZ2"] = {4,5,3,3,4,4,5}
notas["PARCIAL"] = {4,4,5,5,4,5,4}
notas["TALLERES"] = {5,4,4,5,4,5,5}

estudiantes_programacion["notas"] = notas
print(estudiantes_programacion)

print(estudiantes_programacion["notas"]["QUIZ1"])
#LO QUE HICIMOS FUE METER EL DICCIONARIO "NOTAS" DENTRO DEL DICCIONARIO "ESTUDIANTES_PROGRAMACION"


#Generar una copia sin afectar el original:
clases_copia = clases.copy()
print(clases_copia)

#Eliminar un componente (LLAVE) de un diccionario
clases_copia.pop("PROFESORES")
print(clases_copia)

#Eliminar la ultima llave agregada 
clases_copia.popitem()
print(clases_copia)

#Agregar una llave, o si ya existe, sobre escribe su valor
#Agrega llave:
clases_copia.setdefault("COMPUTADORES", ["Apple", "Asus", "Samsung", "Lenovo"])
print(clases_copia)
#Sobre escribe llave:
print(clases_copia.setdefault("COMPUTADORES", ["Apple", "Asus", "Samsung", "Lenovo", "Dell"]))
print(clases_copia)

#Limpiar el contenido de un diccionario por completo:
clases_copia.clear()
print(clases_copia)

#Crear un diccionario con las llaver el valor inicial sera el misjmo para todos
keys = {"idiomas", "carreras"}
values = "soy un valor generico"
diccionario_creado = dict.fromkeys(keys,values)
print(diccionario_creado)

#Crear un diccionario sin un valor inicial (DICCIONARIOS VACIOS):
diccionario_creado = dict.fromkeys(keys)
print(diccionario_creado)

#Obtener la definicion de otra manera directamente en una lista
#Esto me retorna el interior del diccionario en forma de lista automaticamente sin necesidad de hacer la conversion:
print(clases.get("PROFESORES"))
print(estudiantes_programacion.get("Nombres"))


