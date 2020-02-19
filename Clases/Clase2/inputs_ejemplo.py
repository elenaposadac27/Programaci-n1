
#---------------Mensajes----------------
#cuando es informacion en letras se utilizan comillas("")
#int es cuando la respuesta es numero ENTEROS
#float es cuando la respuesta es numeros DECIMALES
PREGUNTA_NOMBRE = "ingrese su nombre \n "
MENSAJE_BIENVENIDO_A = "Bienvenido"
MENSAJE_BIENVENIDO_B = "a este programa"
PREGUNTA_EDAD = "ingrese su edad \n "
MENSAJE_EDAD = "Tu edad es"
PREGUNTA_ESTATURA = "ingrese su estatura \n "
MENSAJE_ESTATURA = "Tu estatura es"
#---------------------------------------


_nombrePersona = input(PREGUNTA_NOMBRE)
print(MENSAJE_BIENVENIDO_A, _nombrePersona, MENSAJE_BIENVENIDO_B)
_edadPersona = int(input(PREGUNTA_EDAD))
print(MENSAJE_EDAD, _edadPersona)
print (type(_edadPersona))
_estaturaPersona = float(input(PREGUNTA_ESTATURA))
print(MENSAJE_ESTATURA, _estaturaPersona)
print (type(_estaturaPersona))
