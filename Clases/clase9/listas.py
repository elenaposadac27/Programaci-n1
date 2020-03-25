#PARA ADICIONAR UNA LISTA A OTRA
#      listaA.extend(listaB)
#Donde listaA es la lista original y listaB la que se va a adicionar

#Ejemplo:
lista_1 = [1,3,5,7,9]
lista_adicionar = ["soy","otra", "lista"]

lista_adicionar.extend(lista_1)
print(lista_adicionar)
#A lista_adicionar se le agregaron los elementos de lista_1


#PARA AGREGAR UN ELEMENTO EN UN PUNTO ESPECIFICO DE LA LISTA
#     lista.inser(posicion,elemento)

#Ejemplo:
lista = [1,5,2,7,3,4,8]

lista.insert(2,900)
print(lista)


#PARA REMOVER UN ELEMENTO QUE TENGA COINCIDENCIA (ELIMINA SOLO EL PRIMERO QUE ENCUENTRE)
#    lista.remove(elemento que se quiere eliminar)

#Ejemplo:
animales = ["vaca", "perro", "cerdo", "conejo", "perro", "caballo"]

animales.remove("perro")
print(animales)


#PARA REMOVER EL ELEMENTO DE UNA POSICION EN ESPECIFICO, PERO PODEMOS ALMACENARLO EN OTRA VARIABLE
#   elemento_eliminado = lista.pop(posicion a eliminar)

#Ejemplo:
elemento_eliminado = animales.pop(1)
print(animales, "el elemento eliminado fue el {} de la posicion dos de la lista" .format(elemento_eliminado))
# el .format me indica que debe ir dentro de los {}


#PARA UBICAR LA PRIMERA POSICION DE DETERMINADO ELEMENTO
#    lista.index(elemento)

#Ejemplo:
print("el animal {} esta ubicado en la posicion {} de la lista".format("conejo",animales.index("conejo")+1),animales)
#ponemos el +1 porque las posiciones inician desde 0


#PARA CONTAR CUANTOS ELEMENTOS IGUALES HAY EN UNA MISMA LISTA
#    lista.count(elemento)

#Ejemplo:
numeros = [2000, 2010, 2003, 2001, 2000, 2015, 2004, 2006, 2004, 2000]

print("en la lista {} aparece el numero {} la siguiente cantidad de veces: {}".format(numeros,2000,numeros.count(2000)))


#PARA CLONAR LISTA (CUANDO UNA MODIFICA EL ELEMENTO CLONADO TAMBIEN MODIFICA EL ORIGINAL Y VISCEVERSA)
#     lista_clonada = lista_original

#Ejemplo:
lista_clonada = numeros
lista_clonada.append("hoy")
print("lista original {} vs lista clonada {}".format(numeros,lista_clonada))


#PARA GENERAR UNA COPIA DE UNA LISTA (AL REALIZAR MODIFICACIONES EN UNA, NO SE AFECTA LA OTRA)
#     lista_copia = lista original.copy()

#Ejemplo:
lista_original = [3,5,7,4,1,6]

lista_copiada = lista_original.copy()
lista_copiada.append("h")
print("lista original {} vs lista copia {}".format(lista_original,lista_copiada))


#PARA ENCONTRAR EL NUMERO MAS GRANDE DE UNA LISTA O EL STRING DE MAXIMO TAMAÑO
#     max(lista)
# Cuando la lista es de strings se hace asi :  max(lista, key=len)

#Ejemplo:
print("El numero mas grande en la lista {} es el {}".format(lista_original,max(lista_original)))

lista_str = ["soy", "otra", "lista"]
print("La palabra mas grande en la lista {} es ´{}´".format(lista_str,max(lista_str, key=len)))


#PARA ORDENAR UNA LISTA:
#CRECIENTE
#   lista.sort()

#DECRECIENTE
#   lista.sort(reverse=true)

#CRECIENTE SEGUN TAMAÑO DE STRINGS
#   lista.sort(key=len)

#DECRECIENTE SEGUN TAMAÑO  DE STINGS
#   lista.sort(key=len, reverse=true)

