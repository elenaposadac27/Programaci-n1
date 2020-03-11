#-----VARIABLES----
NOMBRES = ["Manuela", "Alicia", "Sebastian", "Amalia", "Emilio", "Sofia"]
EDADES = [10, 23, 14, 19, 25, 8]
sumaEdades = 0

#----CODIGO-----
#----Ciclo for en rango:
print(len(NOMBRES), len(EDADES))
for i in range(len(NOMBRES)) :
    if EDADES[i] >= 18 :
        print (i,"La persona", NOMBRES[i], "es mayor de edad")

#----Ciclo for en elementos:
for edad in EDADES :
    sumaEdades = sumaEdades + edad
print(sumaEdades)