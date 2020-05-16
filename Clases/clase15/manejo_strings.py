texto = "qui lorem ipsum quia dolor sit amet onsectetur adipisci velit"
print(texto.split('m'))
#Le estoy diciendo que cada vez que encuentre una 'm' haga un salto

#Para convertir los elementos de una lista en un string: 
#(lo que va entre las ' ' antes de .join me determina que habrá en el string entre cada elemento de la lista, en este caso hay un espacio)
lista = ["hola", "a", "todos"]
string_of_lista = ' '.join(lista)
print(string_of_lista)

#modificar las q por las t (una letra por otra)
print('t'.join(texto.split('q')))
lista_palabras_texto = texto.split()
print(lista_palabras_texto)
print ( max (lista_palabras_texto,key=len))
#Esto retorna que a es más grande por el código ASCII
print(max("ZaWU"))
print(min("ZaWU"))
txt_primera_mayuscula= texto.capitalize()
print(txt_primera_mayuscula)

 #Para poner todo en mayuscula:
txt_mayuscula= texto.upper()
print(txt_mayuscula)

#Para volver a minuscula:
txt= "HOLA A TODOS"
print (txt.casefold())

#Para centrar un texto en medio de cierta cantidad de caracteres.
#Ej: si mi frase tiene 23 caracteres y yo le digo que se centre en medio de 25, va a quedar con un espacio a cada lado
txt= "Quiero ir en otro lugar"
print(txt.center(31))

#Para validar que el ingreso si termina en lo deseado.
#Ej : en este caso verificaremos si el parrafo ingresado finaliza en punto (.)
parrafo = "hola cualquier cosa hola cualquier cosa  algo hola cualquier cosa."
print(parrafo.endswith("."))
#Para encontrar determinada palabra en un texto: 
coordenada_inicio = parrafo.find("algo")
cordenada_final = coordenada_inicio+ len("algo")+1
print(parrafo[coordenada_inicio:cordenada_final])

#VALIDACIONES DE TEXTO:
txt = "AAAA"
print(txt.isnumeric()) #Para saber si es totalmente numerico
print(txt.isalpha()) #Para saber si es totalmente alfabetico
print(txt.isascii()) 
print(txt.isprintable()) #Para saber si es imprimible
print(txt.isupper()) #Para saber si esta en mayuscula

#Para reemplazar una palabra por otra:
txt = "me gusta programar en Java"
print (txt.replace("Java", "Python"))
