import pandas as pd

diccionario =pd.read_csv("balance.csv",encoding='UTF-8', header = 0,delimiter=';').to_dict()
print(diccionario)

mayor_ciudad = max(diccionario["Ciudad"].values(), key=len)
print("\n\n La ciudad con el nombre mas largo es", mayor_ciudad)

menor_ciudad = min(diccionario["Ciudad"].values(), key=len)
print("\n La ciudad con el nombre mas corto es", menor_ciudad)

ganancia_mayor = max(diccionario["Ganancias"].values())
print("\n La ciudad con mayores ganancias es", ganancia_mayor)

perdidas_mayor = max(diccionario["Perdidas"].values())
print("\n La ciudad con mayores perdidas es", perdidas_mayor)