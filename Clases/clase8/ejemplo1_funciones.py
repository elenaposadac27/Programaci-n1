def validar_clave (CLAVE_REAL, _claveIngresada):
    if(CLAVE_REAL == _claveIngresada):
        print("Ingreso exitoso")
        STATE = "clave valida"
    else:
       print("Ingreso denegado")
       STATE = "clave invalida" 
    return STATE

def mostar_lista(lista):
    contador = 1
    for elemento in lista:
        print (contador, "-", elemento)
        contador += 1

intentos = 0
estado = validar_clave(1234, int(input("Ingrese la clave porfavor : ")))
intentos += 1
while (estado != "clave valida" and intentos <3) :
    estado = validar_clave(1234, int(input("Ingrese la clave porfavor : ")))
    intentos += 1

comidas=["carne", "pollo", "huevos", "queso"]
mostar_lista(comidas)