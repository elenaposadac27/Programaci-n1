#-----MENSAJES----
PREGUNTA_EDAD = "Ingrese su edad porfavor \n"
MENSAJE_MAYOR = "Eres mayor de edad"
MENSAJE_MENOR = "Aún eres menor de edad"
#----ENTRADAS-----
_edadUsuario = 0
#----CODIGO-------
_edadUsuario = int(input(PREGUNTA_EDAD))
if (_edadUsuario > 0 and _edadUsuario <= 17) :
    print (MENSAJE_MENOR)
else:
    print (MENSAJE_MAYOR)