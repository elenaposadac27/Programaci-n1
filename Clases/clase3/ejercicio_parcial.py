#----------MENSAJES---------
MENSAJE_BIENVENIDA = "Hola, ingresa tu nombre porfavor \n"
MENSAJE_NOTA = "Ingresa tu nota porfavor \n"
MENSAJE_REPROBADO = "Hasta la vista, intenta de nuevo"
MENSAJE_APROBADO = "Felicitaciones!"
MENSAJE_ERROR = "Calificación no existente"
#--------ENTRADAS----------
_entradaNombre = ""
_entradaNota = 0
#--------CODIGO------------
_entradaNombre = input(MENSAJE_BIENVENIDA)
_entradaNota = float(input(MENSAJE_NOTA))
if ((_entradaNota >= 0) and (_entradaNota < 3)) : 
     print (MENSAJE_REPROBADO)
elif ((_entradaNota >= 3) and (_entradaNota <5)) :
    print (MENSAJE_APROBADO)
else:
    print (MENSAJE_ERROR)