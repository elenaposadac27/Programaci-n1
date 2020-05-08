import matplotlib.pyplot as plt

import pandas as p

year =[2000,2001,2002,2003,2004,2005,2006]
dolar_pesos_colombianos = [1950,1820,1620,1650,1930,2080,2020]
dolar_soles =[250,820,620,350,430,280,920]
dolar_pesos_mexicanos =[50,25,20,50,30,80,20]

plt.plot(year,dolar_pesos_colombianos, ".", color = "r", alpha=0.5)
plt.plot(year,dolar_soles)
plt.plot(year,dolar_pesos_mexicanos)
plt.xlabel("Año")
plt.ylabel("Valor del dolar")
plt.title("EVOLUCION DEL DOLAR")
plt.legend(["Dolar en COP", "Dolar en Soles", "Dolar en MXN"])
plt.savefig("Grafico dolar.png")
plt.close()

###########################################################################
#ELECTROENCEFALOGRAMA:

ecg =p.read_csv("ecg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("ECG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("mi_ecg.png")
plt.close()