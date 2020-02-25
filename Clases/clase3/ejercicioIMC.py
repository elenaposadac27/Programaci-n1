#---------MENSAJES--------
PREGUNTA_NOMBRE = "ingrese su nombre \n"
PREGUNTA_ESTATURA = "ingrese porfavor su estatura \n"
PREGUNTA_PESO = "ingrese porrfavor su peso \n"
MENSAJE_BIENVENIDA_1 = "Bienvenido(a)"
MENSAJE_BIENVENIDA_2 = "iniciemos con la medicion de su IMC"
MENSAJE_NORMAL = "Muy bien, su condición es óptima"
MENSAJE_SOBREPESO = "Usted se encuentra en condición de sobrepeso, debe visitar a su médico"
MENSAJE_OBESIDAD = "Usted presenta un caso de obesidad, porfavor visite a su médico"
MENSAJE_BAJO_PESO = "Usted se encuentra en un rango de bajo peso"
#-------------------------
#--------ENTRADAS---------
_nombreUsuario = " "
_estaturaUsuario = 0
_pesoUsuario = 0
#-------------------------
#---------CODIGO----------
_nombreUsuario = input(PREGUNTA_NOMBRE)
print(MENSAJE_BIENVENIDA_1, _nombreUsuario, MENSAJE_BIENVENIDA_2)
_estaturaUsuario = float (input(PREGUNTA_ESTATURA))
_pesoUsuario = float (input(PREGUNTA_PESO))
if ((_pesoUsuario / (_estaturaUsuario ** 2)) <= 18.5 ) :
    print(MENSAJE_BAJO_PESO)
elif ((_pesoUsuario / (_estaturaUsuario ** 2)) > 18.5  and (_pesoUsuario / (_estaturaUsuario ** 2)) <= 24.9) :
    print(MENSAJE_NORMAL) 
elif ((_pesoUsuario / (_estaturaUsuario ** 2)) >= 25 and (_pesoUsuario / (_estaturaUsuario ** 2)) <= 29) :
    print(MENSAJE_SOBREPESO) 
else:
    print(MENSAJE_OBESIDAD)