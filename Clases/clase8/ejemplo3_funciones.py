def bienvenida():
    print("Bienvenido a su lista de mercado")

def validar_clave (CLAVE_REAL, _claveIngresada):
    if(CLAVE_REAL == _claveIngresada):
        print("Ingreso exitoso")
        STATE = "clave valida"
    else:
       print("Ingreso denegado")
       STATE = "clave invalida" 
    return STATE

def mostar_2_listas(lista_1, lista_2):
    if (len(lista_1) == len(lista_2)):
        for i in range(len(lista_1)):
            print(lista_1[i], "$", lista_2[i])

    else:
        print("No es posible mostar los elementos uno a uno")


def ingreso():
    intentos = 0
    estado = validar_clave(1234, int(input("Ingrese la clave porfavor : ")))
    intentos += 1
    while (estado != "clave valida" and intentos <3) :
        estado = validar_clave(1234, int(input("Ingrese la clave porfavor : ")))
        intentos += 1
    return estado


bienvenida()
if ingreso() == "clave valida" :
    comidas=["carne", "pollo", "huevos", "queso"]
    precios = [12560, 6390, 4500, 2300]
    mostar_2_listas(comidas,precios)
else:
    print("Lo sentimos, no es posible ingresar")