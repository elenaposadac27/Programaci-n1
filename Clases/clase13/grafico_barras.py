#Pyplot es un conjunto de instrucciones que nos permiten desarrollar graficos de diferente indole
import matplotlib.pyplot as plt

import pandas as p 

personas = {"Nombres": ["Carlos", "Isabela", "Adelaida", "Tata", "Nicolas"], "Pesos" : [72,50,43,57,62]}

print(personas["Nombres"])
print(personas["Pesos"])

#Para determinar titulo de la grafica y elementos en x y y (color y alpha me permiten determinar el color de las barras y la tonalidad)
# se utiliza plt.bar para barras VERTICALES y plt.barh para barras HORIZONTALES
 
plt.bar(personas["Nombres"], personas["Pesos"], color = "r", alpha=0.5)
plt.title("Peso de pacientes")
plt.xlabel("Nombres")
plt.ylabel("Pesos (kg)")
plt.savefig("Pesos_pacientes.png")
plt.show()

plt.barh(personas["Nombres"], personas["Pesos"], color = "r", alpha=0.5)
plt.title("Peso de pacientes")
plt.xlabel("Nombres")
plt.ylabel("Pesos (kg)")
#Para determinar el tamaño de la imagen que quiero guardar de la grafica se hace asi: (en pulgadas)
figure = plt.gcf()
figure.set_size_inches(9,9)
plt.savefig("Pesos_pacientes_horizontal.png")
plt.show()

##############################################################################################

barrios = p.read_csv("barrios_medellin.csv", encoding='UTF-8', header=0, delimiter=";").to_dict()
print(barrios)
plt.title("HABITANTES DE LOS BARRIOS DE MEDELLIN", fontsize=20)
plt.bar(barrios["Barrio"].values(),barrios["Habitantes"].values(),align="center")
plt.xlabel("Barrios")
plt.ylabel("Habitantes")
#utilizo xticks para girar los titulitos de cada barra en la coordenada x
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Barrios.png")
plt.show()