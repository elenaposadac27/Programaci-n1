#------MENSAJES-----
MENSAJE_BIENVENIDA = "Sr(a) pasajero, bienvenido al programa de prevencion de coronavirus \n"
PREGUNTA_TEMPERATURA = "Ingrese la temperatura obtenida \n"
PREGUNTA_ORIGEN = "Ingrese el pais de origen del pasajero \n"
MENSAJE_SALUDABLE = "El estado del pasajero es saludable"
MENSAJE_HIPOTERMIA = "El estado del pasajero es de hipotermia"
MENSAJE_ALERTA = "El estado del pasajero es alertable"
MENSAJE_PELIGRO = "El estado del pasajero es peligroso"
MENSAJE_OBSERVACION = "Es necesario poner al pasajero en observacion"
#-----VARIABLES------
_temperaturaPasajero = 0
_origenPasajero = " "
#-----NO VARIABLES----
PAISES_ALERTA = "China, Iran e Italia"
#------CODIGO------
print (MENSAJE_BIENVENIDA)
_origenPasajero = input(PREGUNTA_ORIGEN)
if (_origenPasajero in PAISES_ALERTA) :
    print (MENSAJE_OBSERVACION)
else:
    _temperaturaPasajero = float(input(PREGUNTA_TEMPERATURA)) 
    if (_temperaturaPasajero >= 36 and _temperaturaPasajero <= 38.4) :
        print(MENSAJE_SALUDABLE)
    elif ( _temperaturaPasajero < 36) :
        print(MENSAJE_HIPOTERMIA)
    elif (_temperaturaPasajero >= 38.5 and _temperaturaPasajero < 40) :
        print(MENSAJE_ALERTA)
    else:
        print(MENSAJE_PELIGRO)