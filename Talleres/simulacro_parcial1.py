#---MENSAJES---
MENSAJE_SALTOS = "Ingrese la cantidad de saltos /n"
MENSAJE_CANGURO = "El canguro dio su salto numero"
#--------------

class Canguros():
    def __init__(self,genero,id,edad):
        self.especie = "canguro"
        self.genero = genero
        self.id = id
        self.edad = edad
    
    def saltar(self,saltos):
        for i in range(_cantidadSaltos) :
            print(MENSAJE_CANGURO,i+1)
        
class Cuidador():
    def __init__(self,nombre,id):
        self.nombre = nombre
        self.id = id

    def alimentar_canguros(self):
        print("Es hora del almuerzo, voy a alimentar a los canguros")
        return "Tarea realizada"

class Jefe(Cuidador):
    def contratar(self):
        print("Se necesita un nuevo cuidador para los canguros")
        return "He realizado una nueva contratacion para el zoológico "

    def dar_mensaje_bienvenida(self):
        print("Bienvenidos sean todos al area de canguros del zoológico de la ciudad")
        return "Disfruten su visita"


canguro1 = Canguros("macho", 2001, 10)
canguro2 = Canguros("macho", 2002, 5)
canguro3 = Canguros("hembra", 2003, 8)
canguro4 = Canguros("macho", 2004, 2)
canguro5 = Canguros("hembra", 2005, 2)
canguro6 = Canguros("hembra", 2006, 10)
canguro7 = Canguros("hembra", 2007, 7)
canguro8 = Canguros("hembra", 2008, 4)
canguro9 = Canguros("macho", 2009, 6)
canguro10 = Canguros("macho", 2010, 7)

cuidador1 = Cuidador("Andres", 9315)
cuidador2 = Cuidador("Alicia", 9316)
cuidador3 = Cuidador("Sara", 9317)
cuidador4 = Cuidador("Felipe", 9318)
cuidador5 = Cuidador("Juliana", 9319)
cuidador6 = Jefe("Pedro", 9314)


_cantidadSaltos = 12
canguro5.saltar(_cantidadSaltos)
print("El canguro con código de identificacion", canguro5.id ,"realizo",_cantidadSaltos, "saltos")

bienvenida = cuidador6.dar_mensaje_bienvenida()
print("Mi nombre es", cuidador6.nombre, "y soy el jefe de cuidadores de canguros")
print(bienvenida)
contratacion = cuidador6.contratar()
print(contratacion)

print("Hola soy",cuidador2.nombre,  ", nueva cuidadora de canguros del zoológico con codigo de identificacion", cuidador2.id)
alimentar = cuidador2.alimentar_canguros()
print(alimentar)

