#----LISTAS---
edadesIniciales = [1,2,4,8,16,32,64]
edadesHoy = []

#---ENTRADAS---
_ingresarEdades = ""
sumaEdades = 0
cantidadEdades = 0

#----MENSAJES----
PREGUNTA_INGRESO_EDADES = "¿DESEA AGREGAR LA EDAD DE NUEVOS PACIENTES INGRESADOS? s-->si ó n-->no \n"
MENSAJE_INGRESO_EDADES = "DETERMINE LA EDAD DEL PACIENTE QUE DESEA INGRESAR: \n"
MENSAJE_EDADES_HOY = "EL DIA DE HOY FUERON INGRESADOS PACIENTES CON LAS SIEGUIENTE EDADES : "
MENSAJE_EDADES_TOTALES = "ACTUALEMENTE SE ENCUENTRAN EN EL HOSPITAL PACIENTES CON LAS SIGUIENTES EDADES: \n"
MENSAJE_BIENVENIDA = "¡BIENVENIDO AL SISTEMA DE INGRESO DE PACIENTES!"

#----CODIGO---

print(MENSAJE_BIENVENIDA)
_ingresarEdades = input(PREGUNTA_INGRESO_EDADES)
while (_ingresarEdades == "s" ):
    edadesHoy.append(int(input(MENSAJE_INGRESO_EDADES)))
    _ingresarEdades = input(PREGUNTA_INGRESO_EDADES)
print(MENSAJE_EDADES_HOY, edadesHoy)

edadesIniciales.extend(edadesHoy)
print(MENSAJE_EDADES_TOTALES, edadesIniciales)

for edad in edadesIniciales :
    sumaEdades = sumaEdades + edad

cantidadEdades = int(len(edadesIniciales))
_promedio = sumaEdades / cantidadEdades
print("EN PROMEDIO, LA EDAD DE LOS PACIENTES ES DE {} AÑOS" .format(_promedio))

edadesIniciales.sort(reverse=True)
print("EL PACIENTE MÁS LONGEVO POSEE {} AÑOS".format(max(edadesIniciales)))
print("EL PACIENTE MÁS JOVEN POSEE {} AÑOS".format(edadesIniciales[-1]))
print("LA TOTALIDAD DE EDADES DE LOS PACIENTES ACTUALES DE MANERA DECRECIENTE ES: {}".format(edadesIniciales))

edadesIniciales.sort()
print("LA TOTALIDAD DE EDADES DE LOS PACIENTES ACTUALES DE MANERA CRECIENTE ES: {}".format(edadesIniciales))

edadesIniciales.insert(4,84)
print(MENSAJE_EDADES_TOTALES, edadesIniciales)

edadesIniciales.pop(6)
print("DESPUÉS DE LA SALIDA DE UNO DE NUESTROS PACIENTES,", MENSAJE_EDADES_TOTALES, edadesIniciales)