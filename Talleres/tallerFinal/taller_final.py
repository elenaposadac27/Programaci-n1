import matplotlib.pyplot as plt
import pandas as p 
import sys

def validador_de_archivo(file):
    assert(file)
    return False
validador = True

while(validador):
    file = input("Ingrese el archivo que desea graficar \n")
    try:
        validador = open(file)
        validador = False
    except FileNotFoundError:
      print("Ingresaste un archivo que no existe")


grafico = p.read_csv(file,encoding='UTF-8',header=0, delimiter=";").to_dict()
plt.title(input("Ingrese el titulo que desea darle al grafico: \n"))
x= list(grafico["muestra"].values())
y = list(grafico["valor"].values())
plt.xlabel(input("Ingrese el titulo que desea darle al eje x correspondiente al tiempo \n"))
plt.ylabel(input("Ingrese el titulo que desea darle al eje y correspondiente al voltaje \n"))
plt.plot(x,y)
plt.savefig("grafico_taller_final.png")
plt.close()

##############################################################################################

_nombreUsuario = " "
_estaturaUsuario = 0
_pesoUsuario = 0


try:
    _nombreUsuario = input("Ingrese su nombre \n")
except ValueError:
  print("Ingrese su nombre de manera correcta")


try:
     _estaturaUsuario = float(input("Ingrese su estatura porfavor \n"))
except ValueError:
    print("Ingrese su estatura nuevamente de manera correcta")

    
try:
    _pesoUsuario = float(input("Ingrese su peso porfavor \n"))
except ValueError:
  print("Ingrese su peso nuevamente de manera correcta")

print(_nombreUsuario,"su IMC es", _pesoUsuario / (_estaturaUsuario ** 2))


#######################################################################################3

def validador_parrafo(parrafo):
    assert(parrafo.endswith("."))
    return False
validador = True

while(validador):
     parrafo = input("Mediante un corto parrafo, ponga en palabras porfavor como se siente en este momento. Debe finalizar con . \n")
     try:
         validador = validador_parrafo(parrafo)
     except AssertionError:
         print("Entrada no valida. Recuerde que debe finalizar con .")

###################################################################################

labels = 'Leche', 'Huevo', 'Vino', 'Arroz', 'Queso', 'Salchichas'
sizes = [12, 8, 4, 26, 30, 20]
explode = (0, 0, 0, 0, 0.1, 0)

plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("VENTAS EN UNA TIENDA")
plt.savefig("Grafico_ventas_tienda.png")
plt.close()

####################################################################################

alimentos = {"Productos": ["Arroz", "Lentejas", "Frijoles", "Papa"]}

kilos_arroz = "No ingresaste los kilos de arroz"
try:
    kilos_arroz=float(input("Ingrese la cantidad de kilos que posee de arroz \n"))
except ValueError:
    print("Ingresaste una cantidad invalida correspondiente al peso del arroz")
print("Posees", kilos_arroz, "kilos de arroz")

kilos_lentejas = "No ingresaste los kilos de lentejas"
try:
    kilos_lentejas=float(input("Ingrese la cantidad de kilos que posee de lentejas \n"))
except ValueError:
    print("Ingresaste una cantidad invalida correspondiente al peso de las lentejas")
print("Posees", kilos_lentejas, "kilos de lentejas")

kilos_frijoles = "No ingresaste los kilos de frijoles"
try:
    kilos_frijoles=float(input("Ingrese la cantidad de kilos que posee de frijoles \n"))
except ValueError:
    print("Ingresaste una cantidad invalida correspondiente al peso de frijoles")
print("Posees", kilos_frijoles, "kilos de frijoles")

kilos_papa = "No ingresaste los kilos de papa"
try:
    kilos_papa=float(input("Ingrese la cantidad de kilos que posee de papa \n"))
except ValueError:
    print("Ingresaste una cantidad invalida correspondiente al peso de papa")
print("Posees", kilos_papa, "kilos de papa")

Pesos = (kilos_arroz, kilos_lentejas, kilos_frijoles, kilos_papa)

print(alimentos["Productos"])
print(Pesos)

plt.bar(alimentos["Productos"],Pesos, color = "r", alpha=0.5)
plt.title("CANTIDAD DE PRODUCTOS")
plt.xlabel("Producto")
plt.ylabel("Pesos (kg)")
plt.savefig("grafica_productos_final.png")
plt.close()

