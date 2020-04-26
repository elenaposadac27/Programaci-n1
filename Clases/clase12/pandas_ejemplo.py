import pandas as pd

#Primera entrada nombre de archivo
#Segunda entrada Encoding
#Terecera entrada el header
#delimitador es el caracterecter especial que separa mis datos
#.to_dict transforma mis datos en un diccionario

#Asi: 
#   diccionario =p.read_csv("estudiantes.csv",encoding='UTF-8', header = 0,delimiter=';').to_dict()
#   print(diccionario)

#para imprimir como los titulitos del cuador de excel:
#   print(diccionario.keys())
#para imprimir los datos dentro de determinada columna (los datos dento de la columna de determinado titulito):
#   print(diccionario["Nombre"])

#valor maximo dentro de los datos de determinada columna segun tamaño (longitud de palabras)
#   mayor_nombre = max (diccionario["Nombre"].values(), key=len)
#valor maximo dentro de los datos de determinada columna segun tamaño
#   minimo_nombre = min (diccionario["Nombre"].values(), key=len)

#   print("\n\nel estudiante con el nombre mas largo es {} y el que presenta el nombre mas corto es {} ".format(mayor_nombre, minimo_nombre))


#   estudiante_mayor = max(diccionario["Edad"].values())
#   estudiante_menor = min(diccionario["Edad"].values())
#   print(estudiante_mayor)
#   print(estudiante_menor)
#   nota_mayor = max( diccionario["PARCIAL 2"].values())
#   nota_menor = min( diccionario["PARCIAL 2"].values())
#   print(nota_mayor)
#   print(nota_menor)