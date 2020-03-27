#-----MENSAJES----
PREGUNTA_INGRESO_PESO = "Desea ingresar el peso de un nuevo paciente? s --> si o n --> no \n"
MENSAJE_INGRESO_PESO = "Determine el peso del paciente que desea ingresar : \n"
MENSAJE_SALIDA = "GRACIAS POR UTILIZAR EL SISTEMA DE REGISTRO DE PRESION EN RESPIRADORES!"
MENSAJE_ERROR = "INGRESE PORFAVOR UNA OPCION VALIDA DENTRO DEL MENÚ"
MENSAJE_BIENVENIDA = "BIENVENIDO AL SISTEMA DE CALCULO Y MANEJO DE PRESIONES EN RESPIRADORES"
#-----ENTRADAS---
_pesoPaciente = 0
#-----LISTAS----
pesosPacientesIniciales = [32,64,74,85,98,115,122,127,127,137,148]
presionesPacientes = []
for i in range(len(pesosPacientesIniciales)):
    presionesPacientes.append(pesosPacientesIniciales[i]*6)
#----CODIGO----
def mostar_2_listas(lista_1, lista_2):
    if (len(lista_1) == len(lista_2)):
        for i in range(len(lista_1)):
            print(lista_1[i],  lista_2[i])
    else:
        print("No es posible mostar los elementos uno a uno")

print(MENSAJE_BIENVENIDA)

_menu = int(input("""
    Ingrese:
    1- para ver informacion sobre presiones de pacientes con respecto al peso
    2- para añadir lista de pesos de pacientes
    3- para ver informacion sobre presiones de pacientes
    4- Salir
"""))
while (_menu != 4 ):
    if (_menu == 1):
        print("PESO - PRESION(Hgmm)")
        mostar_2_listas(pesosPacientesIniciales, presionesPacientes)
        
    elif (_menu == 2):
        _pesoPaciente = input(PREGUNTA_INGRESO_PESO)
        while (_pesoPaciente == "s") :
            pesosPacientesIniciales.append(int(input(MENSAJE_INGRESO_PESO)))
            presionesPacientes = []
            for i in range(len(pesosPacientesIniciales)):
                presionesPacientes.append(pesosPacientesIniciales[i]*6)
            _pesoPaciente = input(PREGUNTA_INGRESO_PESO)
        print ("LISTA DE PESOS CORRESPONDIENTE A PACIENTES ACTUALES: ", pesosPacientesIniciales, "kg")
    elif (_menu == 3) :
        presionesPacientes.sort(reverse=True)
        print("La totalidad de las presiones registradas de manera decreciente son: {}".format(presionesPacientes))
        print("La presion más alta registrada entre los pacientes actuales es de {} Hgmm".format(max(presionesPacientes)))
        print("La presion mas baja registrada entre los pacientes actuales es de {} Hgmm".format(presionesPacientes [-1]))
        print("Se han registrado {} presiones el día de hoy".format(len(presionesPacientes)))
    else:
        print(MENSAJE_ERROR)
    _menu = int(input("""
    Ingrese:
    1- para ver informacion sobre presiones de pacientes con respecto al peso
    2- para añadir lista de pesos de pacientes
    3- para ver informacion sobre presiones de pacientes
    4- Salir
    """))

print(MENSAJE_SALIDA)
        