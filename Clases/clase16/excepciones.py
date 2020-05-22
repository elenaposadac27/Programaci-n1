import sys

edad = "No ingresaste edad"
try:
     edad = int(input("ingrese su edad:"))
except ValueError:
    print("ingresaste mal la edad")

print("Hola, tu edad es", edad)

try: 
     archivo = open("Soy_un_archivo_que_no_existe.txt")
except FileNotFoundError:
    print("Ingresaste un archivo que no existe")

#assert() valida que algo sea cierto #so (sistema operativo)
def os_validate(so):
    assert(so in sys.platform)
    print("Estas en el sistema operativo", so)

try:
    os_validate("linux")
except AssertionError:
    print("No eres linux")

try:
    os_validate("win32")
except AssertionError:
    print("No eres windows")



def validador_parrafo(parrafo):
    assert(parrafo.endswith("."))
    return False
validador = True

while(validador):
     parrafo = input("ingrese un parrafo. Debe finalizar con . \n")
     try:
         validador = validador_parrafo(parrafo)
     except AssertionError:
         print("Entrada no valida")

