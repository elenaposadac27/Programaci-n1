#------Anotaciones-----
#Se utiliza for para ciclos en los que conocemos el numero de repeticiones del ciclo
#        Ej:      for i in range(numero de ciclos) :
#for i in range se utiliza cuando necesitaré la posicion
#for elementos se utiliza para poder mostrar los elementoos u obtener resultados de ellos

#--EJEMPLO1---
#-----MENSAJES-----
MENSAJE_SALTOS = "Ingrese la cantidad de saltos : "
MENSAJE_CANGURO = "El canguro dio su salto numero"
#-----VARIABLES-----
_cantidadSaltos = 0

#-----CODIGO------
_cantidadSaltos = int (input(MENSAJE_SALTOS))
for i in range(4) :
 print (i)
#--ó---
for i in range(_cantidadSaltos) :
    print(MENSAJE_CANGURO,i+1)


#--EJEMPLO2---
#------VARIABLES----
DIAS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
#----CODIGO----
for dia in DIAS :
    print(dia)