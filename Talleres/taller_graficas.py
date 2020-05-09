import matplotlib.pyplot as plt
import pandas as p

consumos = p.read_csv("consumos_barrios.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(consumos)

plt.bar(consumos["Barrio"].values(), consumos["Agua"].values(), color = "r", alpha=0.5)
plt.title("CONSUMO DE AGUA EN LOS BARRIOS DE MEDELLIN")
plt.xlabel("Barrio")
plt.ylabel("Agua")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Grafico_consumo_agua.png")
plt.close()

plt.bar(consumos["Barrio"].values(), consumos["Gas"].values(), color = "r", alpha=0.5)
plt.title("CONSUMO DE GAS EN LOS BARRIOS DE MEDELLIN")
plt.xlabel("Barrio")
plt.ylabel("Gas")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Grafico_consumo_gas.png")
plt.close()



ecg = p.read_csv("ecg_taller.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(ecg)

x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("ELECTROENCFALOGRAMA")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("Grafico_ecg_taller.png")
plt.close()

#####Pueden verse 6 picos altos en el electroencefalograma

labels = 'Bogota', 'Medellin', 'Leticia', 'Villavicencio'
sizes = [80, 7, 5, 8]
explode = (0, 0, 0.5, 0)
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("CASOS DE COVID-19 EN COLOMBIA")
plt.savefig("Grafico_casos_pie.png")
plt.close()

