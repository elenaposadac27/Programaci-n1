#-------VARIABLES-------
listaNombres = ["Santiago", 
"Marco", 
"Juan Esteban", 
"MCH Betancur", 
"MCH Mesa", 
"David", 
"Susana", 
"Ysabella", 
"Santiago H", 
"Maria Fernanda", 
"Daniel", 
"Leslly", 
"Elena", 
"Daniel H"]

listaEdades = [20,
19,
16,
19,
20,
21,
20,
19,
19,
18,
19,
18,
19,
26]

listaNotas = [4.4,
2.3,
3.2,
4,
4.2,
3.5,
5,
4.6,
5,
4.4,
4.7,
3.4,
4.8,
5]

#------CODIGO-------
_decision = int(input("""
    Ingrese:
    1- para ver lista de nombres
    2- para ver edades
    3- para ver notas
    4- Salir
"""))
while (_decision != 4) :
    if (_decision == 1):
        print(listaNombres)
    elif (_decision == 2) :
        print (listaEdades)
    elif (_decision == 3) :
        print (listaNotas)
    else:
        print ("Ingrese un valor valido")
    _decision = int(input("""
        Ingrese:
      1- para ver lista de nombres
      2- para ver edades
      3- para ver notas
      4- Salir
      """))
print("Gracias por usar el programa")