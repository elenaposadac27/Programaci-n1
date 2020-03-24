#-----MENSAJES----
MENSAJE_MEDICOS = "INGRESE LOS MEDICOS EN TURNO EN LA SALA DE URGENCIAS: \n"
MENSAJE_ENFERMERIA = "INGRESE EL PERSONAL DE ENFERMERIA DISPONIBLE EN LA SALA DE URGENCIAS: \n"
MENSAJE_PACIENTES = "INGRESE EL NOMBRE DEL PACIENTE:\n"
MENSAJE_ESTADO_PACIENTE = "DETERMINE LA CATEGORIA DE TRIAGE DE CADA UNO DE LOS PACIENTES EN ORDEN DE INGRESO (1, 2, 3, 4 ó 5): \n"
MENSAJE_ERROR = "INGRESE UNA OPCION VALIDA DENTRO DEL MENÚ"
MENSAJE_SALIDA = "GRACIAS POR UTILIZAR EL SISTEMA DE LA UNIDAD DE URGENCIAS"

#-----FUNCIONES-----
def bienvenida():
    print("Bienvenido(a) al sistema de la unidad de urgencias")

def llenar_lista():
    lista = []
    decision = input("Ingrese s --> para agregar más elementos, n --> para NO agregar más elementos :")
    while (decision == "s"):
        lista.append(input("Ingrese un elemento de la lista: "))
        decision = input("Ingrese s --> para agregar más elementos, n --> para NO agregar más elementos :")
    return lista

def mostar_lista(lista):
    contador = 1
    for elemento in lista:
        print (contador, "-", elemento)
        contador += 1

def mostar_2_listas(lista_1, lista_2):
    if (len(lista_1) == len(lista_2)):
        contador = 1
        for i in range(len(lista_1)):
            print("PACIENTE-TRIAGE")
            print(contador, "-", lista_1[i], lista_2[i])
            contador += 1


#-----CODIGO----
bienvenida()
_menuIngreso = int(input("""
    Ingrese el tipo de personal que desea ingresar:
    1- PERSONAL MÉDICO
    2- ENFERMERÍA
    3- PACIENTES
    4- Visualizar listas
    5- Salir \n
"""))

while (_menuIngreso != 5) :
    if (_menuIngreso == 1):
        print (MENSAJE_MEDICOS)
        medicos = llenar_lista()

    elif (_menuIngreso == 2):
        print(MENSAJE_ENFERMERIA)
        enfermeria = llenar_lista()

    elif (_menuIngreso == 3):
        print(MENSAJE_PACIENTES)
        pacientes = llenar_lista()
        print(MENSAJE_ESTADO_PACIENTE)
        estado = llenar_lista()
    
    elif(_menuIngreso == 4):
        _menuVisualizacion = int(input("""
            Ingrese el tipo de personal que desea visualizar:
            1- PERSONAL MÉDICO
            2- ENFERMERÍA
            3- PACIENTES
            4- Salir \n
         """))

        while (_menuVisualizacion != 4) :
            if (_menuVisualizacion == 1):
                 mostar_lista(medicos)

            elif (_menuVisualizacion == 2):
                 mostar_lista(enfermeria)
        
            elif (_menuVisualizacion == 3):
                 mostar_2_listas(pacientes,estado)

            else:
                print(MENSAJE_ERROR)

            _menuVisualizacion = int(input("""
               Ingrese el tipo de personal que desea visualizar:
                1- PERSONAL MÉDICO
                2- ENFERMERÍA
                3- PACIENTES
                4- Salir \n
                """))
        print(MENSAJE_SALIDA)
        
    else:
        print(MENSAJE_ERROR)


    _menuIngreso = int(input("""
    Ingrese el tipo de personal que desea ingresar:
    1- PERSONAL MÉDICO
    2- ENFERMERÍA
    3- PACIENTES
    4- Visualizar listas
    5- Salir \n
    """))

print(MENSAJE_SALIDA)


