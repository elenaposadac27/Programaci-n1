import pandas as pd
diccionario =pd.read_csv("barrios.csv",encoding='UTF-8', header = 0,delimiter=';').to_dict()
print(diccionario)

barrio_largo = max(diccionario["Barrio"].values(), key=len)
print("\n\n El barrio con el nombre mas largo es", barrio_largo)

barrio_corto = min(diccionario["Barrio"].values(), key=len)
print("\n El barrio con el nombre mas corto es", barrio_corto)


mayor_agua = max(diccionario["Agua"].values())
print("\n\n El mayor consumo de agua registrado en los barrios de Medellin es", mayor_agua)

mayor_energia = max(diccionario["Energía"].values())
print("\n El mayor consumo de energia registrado en los barrios de Medellin es", mayor_energia)

mayor_gas = max(diccionario["Gas"].values())
print("\n El mayor consumo de gas registrado en los barrios de Medellin es", mayor_gas)

mayor_internet = max(diccionario["Internet"].values())
print("\n El mayor consumo de internet registrado en los barrios de Medellin es", mayor_internet)


menor_agua = min(diccionario["Agua"].values())
print("\n\n El menor consumo de agua registrado en los barrios de Medellin es", menor_agua)

menor_energia = min(diccionario["Energía"].values())
print("\n El menor consumo de energia registrado en los barrios de Medellin es", menor_energia)

menor_gas = min(diccionario["Gas"].values())
print("\n El menor consumo de gas registrado en los barrios de Medellin es", menor_gas)

menor_internet = min(diccionario["Internet"].values())
print("\n El menor consumo de internet registrado en los barrios de Medellin es", menor_internet)


mayor_habitantes = max(diccionario["Habitantes"].values())
print("\n\n La mayor cantidad de habitantes registrada entre los barrios de Medellín es", mayor_habitantes)

menor_habitantes = min(diccionario["Habitantes"].values())
print("\n La menor cantidad de habitantes registrada entre los barrios de Medellín es", menor_habitantes)