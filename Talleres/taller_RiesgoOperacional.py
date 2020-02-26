#------MENSAJE--------
PREGUNTA_PACIENTES = "Ingrese porfavor el número de pacientes \n"
PREGUNTA_UCI = "Ingrese porfavor el número de pacientes en UCI \n"
MENSAJE_ALTO = "Su riesgo operacional es alto el día de hoy"
MENSAJE_MEDIO = "Su riesgo operacional es medio el día de hoy"
MENSAJE_BAJO = "Su riesgo operacional es bajo el día de hoy"
#---------------------
#------ENTRADAS-------
_numeroPacientes = 0
_numeroPacientesUCI = 0
#---------------------
#-------CODIGO--------
_numeroPacientes = int (input(PREGUNTA_PACIENTES))
if (_numeroPacientes > 0 and _numeroPacientes <= 1000) :
    print (MENSAJE_BAJO)
elif (_numeroPacientes <= 5000):
    _numeroPacientesUCI = int(input (PREGUNTA_UCI))
    if (_numeroPacientesUCI >1000) :
        print (MENSAJE_ALTO)
    else:
        print (MENSAJE_MEDIO)
else:
    print (MENSAJE_ALTO)
