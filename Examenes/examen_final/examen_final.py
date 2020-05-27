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
plt.savefig(input("Ingrese el nombre con el que desea guardar el archivo y adicione .png al final \n"))
plt.show()

######################################################################################################

datos = {"Examen": ["ECG", "EEG", "PPG"], "Picos" : [9,10,9]}

plt.bar(datos["Examen"], datos["Picos"], color = "r", alpha=0.5)
plt.title("RESULTADOS DE EXAMENES SEGUN CANTIDAD DE PICOS")
plt.xlabel("Examen")
plt.ylabel("Picos")
plt.savefig("picos_examenes.png")
plt.show()

######################################################################################################

_nombreUsuario = " "
_estaturaUsuario = 0
_pesoUsuario = 0
_edadUsuario = 0

try:
    _nombreUsuario = input("Ingrese su nombre \n")
except ValueError:
  print("Ingrese su nombre de manera correcta")

try:
    _edadUsuario = int(input("Ingrese su edad porfavor \n"))
except ValueError:
    print("Ingrese su edad nuevamente de manera correcta")


try:
     _estaturaUsuario = float(input("Ingrese su estatura porfavor \n"))
except ValueError:
    print("Ingrese su estatura nuevamente de manera correcta")

    
try:
    _pesoUsuario = float(input("Ingrese su peso porfavor \n"))
except ValueError:
  print("Ingrese su peso nuevamente de manera correcta")

print(_nombreUsuario,"su IMC es", _pesoUsuario / (_estaturaUsuario ** 2))

##############################################################################

labels = 'Habitacion', 'Patio', 'Baño', 'Estudio', 'Cocina'
sizes = [55,20,10,7,8]
explode = (0.1, 0, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("LUGARES DE PERMANENCIA EN CASA")
plt.savefig("Grafico_permanencia_en_casa.png")
plt.show()

##############################################################################

# El APRENDIZAJE SUPERVISADO es aquel en el que se brida en el codigo las condiciones, instrucciones o los patrones que se
#deben seguir para llegar a determinadas conclusiones.
#
#   Por ejemplo: la clasificacion de un grupo de animales segun determinadas caracteristicas que ya fueron brindadas al algoritmos

#El APRENDIZAJE NO SUPERVISADO hace referencia a aquel en el que no se le brinda instrucciones especificas que guien
#de alguna manera las conclusiones a las que se llega.
#Se basa en que la maquina o el algoritmo logre identifica por si solo las características comunes de la informacion entregada y 
#con base a esto tome sus propias decisiones.
#Esta muy estrechamente relacionado con la inteligencia artifical.
