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
ser_humano_2 = Humano("Isabela", 1.60, 48, "femenino", 15)
ser_humano_3 = Humano("Adelaida", 1.62, 45, "femenino", 15)

print(ser_humano.nombre)
print(ser_humano.raza)
print(ser_humano.estatura)
print(ser_humano.peso,"kg")
print(ser_humano.genero)
print(ser_humano.edad, "años")

print(ser_humano_2.nombre)
print(ser_humano_2.raza)
print(ser_humano_2.estatura)
print(ser_humano_2.peso,"kg")
print(ser_humano_2.genero)
print(ser_humano_2.edad, "años")

print(ser_humano_3.nombre)
print(ser_humano_3.raza)
print(ser_humano_3.estatura)
print(ser_humano_3.peso, "kg")
print(ser_humano_3.genero)
print(ser_humano_3.edad, "años")
