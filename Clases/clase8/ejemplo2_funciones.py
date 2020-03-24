comidas = ["carne", "pollo", "huevos", "queso"]
precios = [12560, 6390, 4500, 2300]

def mostar_2_listas(lista_1, lista_2):
    if (len(lista_1) == len(lista_2)):
        for i in range(len(lista_1)):
            print(lista_1[i], "$", lista_2[i])

    else:
        print("No es posible mostar los elementos uno a uno")

mostar_2_listas(comidas,precios)