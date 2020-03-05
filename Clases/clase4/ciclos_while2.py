import random
#-----MENSAJES-------
PREGUNTA_NUMERO = "Ingrese un numero entero entre el 1 y el 10 \n"
MENSAJE_FALLO = "FALLASTE! SIGUE INTENTANDO"
MENSAJE_ACIERTO = "FELICIDADES! SABES MI NUMERO FAVORITO"
MENSAJE_MAYOR = "ESTAS CERCA! BAJA UN POCO"
MENSAJE_MENOR = "EL NUMERO QUE BUSCAS ES UN POCO MAYOR"
#-----NO VARIABLES-----
NUMERO_FAVORITO = random.randint(1,10)
#-----ENTRADAS-------
_numeroIngresado = 0

#------CODIGO------
_numeroIngresado = int (input(PREGUNTA_NUMERO))
while (_numeroIngresado != NUMERO_FAVORITO) :
    print(MENSAJE_FALLO)
    if (_numeroIngresado > NUMERO_FAVORITO) :
        print (MENSAJE_MAYOR)
    else: print (MENSAJE_MENOR)
    _numeroIngresado = int (input(PREGUNTA_NUMERO))
print(MENSAJE_ACIERTO)