#Preguntar
# if (pregunta) :  
# elif (pregunta):  para segunda opcion
# else :   se utiliza cuando ya no hay ninguna opcion
#los dos puntos significan ENTONCES

#-------------MENSAJES---------------------------
PREGUNTA_NOMBRE = "ingrese su nombre \n"
PREGUNTA_EDAD = "ingrese porfavor su edad \n"
MENSAJE_BIENVENIDO = "Bienvenido"
MENSAJE_DESPEDIDA = "CHAO"
MENSAJE_TOCAYO = "Hola, somos tocayos"
MENSAJE_JOVEN = "Eres joven"
MENSAJE_ADULTO = "Eres adulto"
MENSAJE_ADULTO_MAYOR = "Eres adulto mayor"
#------------------------------------------------
#---------- NO VARIABLES-------------------------
NOMBRE_PERSONAL = "Elena"
#------------------------------------------------
#-----------ENTRADAS-----------------------------
_nombreUsuario = ""
_edadUsuario = 0
#------------------------------------------------

#-----------CODIGO-------------------------------
print(MENSAJE_BIENVENIDO)
_nombreUsuario = input(PREGUNTA_NOMBRE)
if (NOMBRE_PERSONAL == _nombreUsuario) :
    print(MENSAJE_TOCAYO)

_edadUsuario = int (input(PREGUNTA_EDAD))
if ((_edadUsuario >= 0) and (_edadUsuario <= 25)) :
    print(MENSAJE_JOVEN)
elif ((_edadUsuario >= 26) and (_edadUsuario <= 65)) :
    print(MENSAJE_ADULTO)
else :
    print (MENSAJE_ADULTO_MAYOR)
print (MENSAJE_DESPEDIDA)