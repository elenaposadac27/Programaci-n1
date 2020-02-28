#-----MENSAJES----
PREGUNTA_EDAD = "Ingrese su edad porfavor \n"
PREGUNTA_INGRESOS = "Ingrese el valor de sus ingresos mensuales \n"
MENSAJE_TRIBUTAR = "Tienes la obligacion de tributar"
MENSAJE_NO_TRIBUTAR = "Aun no es necesario que pagues impuestos"
#-----ENTRADAS----
_edadUsuario = 0
_ingresosUsuario = 0
#-----CODIGO------
_edadUsuario = int(input(PREGUNTA_EDAD))
if (_edadUsuario >= 16) :
    _ingresosUsuario = float(input(PREGUNTA_INGRESOS))
    if (_ingresosUsuario >= 1000) :
        print (MENSAJE_TRIBUTAR)
    else:
        print (MENSAJE_NO_TRIBUTAR)
else:
    print (MENSAJE_NO_TRIBUTAR)
