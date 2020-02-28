#-----MENSAJES-----
MENSAJE_BIENVENIDA = "Bienvenido al programa de cálculo de peso de envio"
PREGUNTA_PAYASOS = "Ingrese el numero de payasos que serán enviados porfavor \n"
PREGUNTA_MUÑECAS = "Ingrese el numero de muñecas que serán enviadas porfavor \n"
MENSAJE_CALCULO = "El peso total del envio es de "
MENSAJE_CALCULO2 = "gramos"
#-----ENTRADAS-----
_cantidadPayasos = 0
_cantidadMuñecas = 0
#-----NO VARIABLES------
PESO_PAYASO = 112
PESO_MUÑECA = 75
#-----CODIGO-------
print(MENSAJE_BIENVENIDA)
_cantidadPayasos = int (input(PREGUNTA_PAYASOS))
_cantidadMuñecas = int (input(PREGUNTA_MUÑECAS))
print(MENSAJE_CALCULO, (_cantidadMuñecas*PESO_MUÑECA)+(_cantidadPayasos*PESO_PAYASO), MENSAJE_CALCULO2)