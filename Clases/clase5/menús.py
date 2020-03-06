#-------Anotaciones------
#Se utiliza [] para determinar la lista de elementos
#Cada elemento dentro de los corches debe ir entre comillas "" si son cosas. LOS NUMEROS NO VAN CON COMILLAS
#    Ejemplo : Lista_mercado = ["huevos", "pan", 5000, "leche", "carne"]
#Los elementos en una lista se empiezan a contar desde el cero (0); es decir que el quinto elemento en la lista es el numero 4

#Para ver el elemento que se encutra en una posicion :
#       print(lista_mercado [3])

#Para reemplazar un elemento en determinada posicion de la lista :
#       Lista_mercado[posicion que quiero reemplazar] = "por lo que lo voy a reemplazar"
#    Ejemplo :  Lista_mercado[3] = "salchichas"

#Para agregar un elemento a la lista : (este elemento quedadar en ultima posicion)
#       Lista_mercado.append("elemento a agregar")

#Para eliminar un elemento de la lista en determinada posicion :
#       Lista_mercado.pop(2)

#Para conocer el numero de elementos dentro de una lista :
#       print(len(lista_mercado))

#TUPLAS : Se utilizan cuando hay algo que no queremos que pueda ser cambiado
#       tupla = (elementos que no podran cambiarse)


#-------VARIABLES-------
listaNombres = ["Santiago", 
"Marco", 
"Juan Esteban", 
"MCH Betancur", 
"MCH Mesa", 
"David", 
"Susana", 
"Ysabella", 
"Santiago H", 
"Maria Fernanda", 
"Daniel", 
"Leslly", 
"Elena", 
"Daniel H"]

#-------CODIGO-------
print(listaNombres)
print (listaNombres[2])
listaNombres[3] = "Maria Camila Betancur"
listaNombres[4] = "Maria Camila Mesa"
print(listaNombres)
listaNombres.pop(13)
print(listaNombres)
listaNombres.append("Daniel Herrera")
print(listaNombres)