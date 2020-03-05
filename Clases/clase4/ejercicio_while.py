import random
#--------MENSAJE------
MENSAJE_12 = "Lograste sumar 12 con tus dados"
#--------NO VARIABLES------
Dado1 = random.randint(1,6)
Dado2 = random.randint(1,6)
SUMA = (Dado1 + Dado2)

#-------CODIGO------
while (SUMA != 12) :
    print (SUMA)
    Dado1 = random.randint(1,6)
    Dado2 = random.randint(1,6)
    SUMA = (Dado1 + Dado2)
    print(SUMA)
print (MENSAJE_12)