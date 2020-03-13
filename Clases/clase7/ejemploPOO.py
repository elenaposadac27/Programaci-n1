#PROGRAMACION ORIENTADA A OBJETOS (POO)
# Las clases son como moldes, y siempre deben ir nombradas con mayuscula inicial
# self. se utiliza para designar todas las caracteristicas o atributos del molde

class Humano():
    def __init__(self, nombre):
        
        self.raza = "ser humano"
        self.nombre = nombre
    
ser_humano = Humano("Elena")
ser_humano_2 = Humano("Isabela")

print(ser_humano.nombre)
print(ser_humano.raza)
print(ser_humano_2.nombre)
print(ser_humano_2.raza)