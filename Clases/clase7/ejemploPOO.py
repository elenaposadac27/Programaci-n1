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

print("Mi nombre es ", ser_humano.nombre)
print("Soy un ", ser_humano.raza)
print("Mido ", ser_humano.estatura)
print("Peso ", ser_humano.peso,"kg")
print("Correspondo al genero ", ser_humano.genero)
print("Tengo ", ser_humano.edad, "años")

print("Mi nombre es ",ser_humano_2.nombre)
print("Soy un ", ser_humano_2.raza)
print("Mido ", ser_humano_2.estatura)
print("Peso ", ser_humano_2.peso,"kg")
print("Correspondo al genero ", ser_humano_2.genero)
print("Tengo ", ser_humano_2.edad, "años")

print("Mi nombre es ", ser_humano_3.nombre)
print("Soy un ", ser_humano_3.raza)
print("Mido ", ser_humano_3.estatura)
print("Peso ", ser_humano_3.peso, "kg")
print("Correspondo al genero ", ser_humano_3.genero)
print("Tengo ", ser_humano_3.edad, "años")
