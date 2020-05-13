import matplotlib.pyplot as plt
import pandas as p 

inventario = p.read_csv("inventario.csv", encoding='UTF-8', header=0, delimiter=";").to_dict()
print(inventario)
plt.title("EXISTENCIA DE ELEMENTOS", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Unidades"].values(),align="center", color = "r", alpha=0.5)
plt.xlabel("Elementos")
plt.ylabel("Cantidad")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Inventario actual.png")
plt.close()

plt.title("EXISTENCIA DE UNIDADES VIEJAS", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Viejo"].values(),align="center", color = "b", alpha=0.5)
plt.xlabel("Elementos")
plt.ylabel("Cantidad")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Inventario viejos.png")
plt.close()

plt.title("EXISTENCIA DE UNIDADES NUEVAS", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Nuevos"].values(),align="center", color = "g", alpha=0.5)
plt.xlabel("Elementos")
plt.ylabel("Cantidad")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Inventario nuevos.png")
plt.close()

ppg = p.read_csv("ppg.csv", encoding='UTF-8', header=0, delimiter=";").to_dict()
print(ppg)
x= list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title("FOTOPLETISMOGRAFIA")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("ppg_paciente.png")
plt.close()

#En la fotopletismografia pueden verse 9 picos altos

labels = 'Recuperandose en casa', 'Hospitalizacion', 'UCI'
sizes = [85,10,5]
explode = (0, 0, 0.1)
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("ESTADO DE PACIENTES COVID-19")
plt.savefig("Grafico_pie_pacientes.png")
plt.show()