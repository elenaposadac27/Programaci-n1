#Guarda en memoria el archivo para su posterior uso
#la 'r' indica que vamos a abrir el archivo en modo lectura(read)
archivo = open("libro.txt",'r')
print(archivo)

#Toma el archivo de corrido
x= archivo.read()
print(x)

#Toma cada letra como una coordenada
letras_archivo = archivo.read()
print(letras_archivo[0])
#print(letras_archivo[posicion deseada])


#Toma cada linea como una coordenada
lineas_archivo = archivo.read().splitlines()
print(lineas_archivo[0])

#Preguntar si en determinada coordenada esta determinado elemento
lineas_archivo = archivo.read().splitlines()
print("sentido" in lineas_archivo[0])

#print(lines_archivo [posicion linea][posicion letra dentro de esa linea])
print(lineas_archivo[0][1])

