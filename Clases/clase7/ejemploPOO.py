#PROGRAMACION ORIENTADA A OBJETOS (POO)
# Las clases son como moldes, y siempre deben ir nombradas con mayuscula inicial
# self. se utiliza para designar todas las caracteristicas o atributos del molde
# __init__ se utiliza para crear objetos de  ese molde y lo que va dentro del () son las caracteristicas propias que se definiran de cada uno

class Humano():
    def __init__(self, nombre, estatura, peso, genero, edad):
        
        self.raza = "ser humano"
        self.nombre = nombre
        self.estatura = estatura
        self.peso = peso
        self.genero = genero
        self.edad = edad
    
ser_humano = Humano("Elena", 1.68, 50, "femenino", 19)
ser_humano_2 = Humano("Isabela", 1.60, 40, "femenino", 15)

print(ser_humano.nombre)
print(ser_humano.raza)
print(ser_humano_2.nombre)
print(ser_humano_2.raza)