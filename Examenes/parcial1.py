#------MENSAJES-----
PREGUNTA_CLASES_ESTUDIANTES= "Ingrese porfavor el numero de clases a las que ha asistido el día de hoy: \n"
MENSAJE_CLASES_ESTUDIANTES= "El estudiante asistió a su clase número  : \n"
PREGUNTA_CLASES_PROFESOR= "Ingrese porfavor el numero de clases que dictará el día de hoy: \n"
MENSAJE_CLASES_PROFESOR= "El profesor dictó su clase número  : \n"
MESNAJE_BIENVENIDA = "Bienvenid@ a la base de datos de la universidad"
MENSAJE_ERROR = "Ingrese una opcion disponible en el menú"
MENSAJE_SALIDA = "Gracias por utilizar el sistema de base de datos de la universidad"

#-----ENTRADAS------
_clasesAsistidas = 0
_clasesDictadas = 0
class Estudiante():
    def __init__(self,nombre,edad,genero,colegio):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.colegio = colegio

    def asistir_clase(self,_clasesAsistidas):
       _clasesAsistidas = int(input(PREGUNTA_CLASES_ESTUDIANTES))
       for i in range(_clasesAsistidas) :
           print (MENSAJE_CLASES_ESTUDIANTES,i+1)
       print("El estudiante asistió a", _clasesAsistidas, "clases el día de hoy")
       return "La jornada del estudiante ha finalizado"

class Profesor():
    def __init__(self,nombre,edad,nivel):
        self.nombre = nombre
        self.edad = edad
        self.nivel = nivel

    def dictar_clase(self,_clasesDictadas):
      _clasesDictadas = int(input(PREGUNTA_CLASES_PROFESOR))
      for i in range(_clasesDictadas) :
         print (MENSAJE_CLASES_PROFESOR,i+1)
      print ("El profesor dictó", _clasesDictadas, "clases el día de hoy")
      return "La jornada del profesor ha finalizado"

class Director(Profesor):
    def contratar(self,nombre,edad,nivel):
        print("Es necesario realizar la contratacion de un nuevo profesor para la universidad")
        new_profesor = Profesor(nombre,edad,nivel)
        print("He contratado al profesor(a) {}. Tiene {}años y cuenta con {}".format(new_profesor.nombre,edad,nivel))
        return new_profesor

estudiante1 = Estudiante("Sofia",18,"femenino","Pinares")
estudiante2 = Estudiante("Emilio",20,"masculino","San José de las Vegas")
estudiante3 = Estudiante("Pedro", 20, "masculino", "Montessori")
estudiante4 = Estudiante("Elena", 19, "femenino", "San José de las Vegas")
estudiante5 = Estudiante("Felipe",19, "masculino", "San Ignacio" )

profesor1 = Profesor("Sandra", 29, "Maestría")
profesor2 = Profesor("Mauricio", 35, "Doctorado")
profesor1 = Profesor("Sandra", 29, "Maestría")
profesor2 = Profesor("Mauricio", 35, "Doctorado")

director1 = Director("Ivan", 40, "Doctorado")

print("ESTUDIANTE 1:")
estudiante1.asistir_clase(_clasesAsistidas)
print("ESTUDIANTE 2:")
estudiante2.asistir_clase(_clasesAsistidas)
print("ESTUDIANTE 3:")
estudiante3.asistir_clase(_clasesAsistidas)
print("ESTUDIANTE 4:")
estudiante4.asistir_clase(_clasesAsistidas)
print("ESTUDIANTE 5:")
estudiante5.asistir_clase(_clasesAsistidas)

print("PROFESOR 1:")
profesor1.dictar_clase(_clasesDictadas)
print("PROFESOR 2:")
profesor2.dictar_clase(_clasesDictadas)

print("DIRECTOR:")
director1.contratar("Marcela",33,"Doctorado")
director1.contratar("Carolina",29,"Maestria")

print(MESNAJE_BIENVENIDA)
_menuIngreso = int(input("""
    Ingrese el tipo de informacion que desea visualizar:
    1- ESTUDIANTES
    2- PROFESORES
    3- DIRECTOR
    4- Salir \n
"""))

while(_menuIngreso != 4) :
    if(_menuIngreso == 1):
     print("ESTUDIANTE 1:")
     print("Mi nombre es", estudiante1.nombre)
     print("Tengo", estudiante1.edad, "años")
     print("Correspongo al genero", estudiante1.genero)
     print("Me gradué del colegio", estudiante1.colegio)

     print("ESTUDIANTE 2:")
     print("Mi nombre es", estudiante2.nombre)
     print("Tengo", estudiante2.edad, "años")
     print("Correspongo al genero", estudiante2.genero)
     print("Me gradué del colegio", estudiante2.colegio)

     print("ESTUDIANTE 3:")
     print("Mi nombre es", estudiante3.nombre)
     print("Tengo", estudiante3.edad, "años")
     print("Correspongo al genero", estudiante3.genero)
     print("Me gradué del colegio", estudiante3.colegio)

     print("ESTUDIANTE 4:")
     print("Mi nombre es", estudiante4.nombre)
     print("Tengo", estudiante4.edad, "años")
     print("Correspongo al genero", estudiante4.genero)
     print("Me gradué del colegio", estudiante4.colegio)

     print("ESTUDIANTE 5:")
     print("Mi nombre es", estudiante5.nombre)
     print("Tengo", estudiante5.edad, "años")
     print("Correspongo al genero", estudiante5.genero)
     print("Me gradué del colegio", estudiante5.colegio)

    elif (_menuIngreso == 2):
        print("PROFESOR 1:")
        print("Mi nombre es", profesor1.nombre, ",tengo", profesor1.edad, "años, y mi nivel educatido es", profesor1.nivel)

        print("PROFESOR 2:")
        print("Mi nombre es", profesor2.nombre, ",tengo", profesor2.edad, "años, y mi nivel educatido es", profesor2.nivel)


    elif (_menuIngreso == 3):
        print("DIRECTOR:")
        print("Mi nombre es", director1.nombre, ",tengo", director1.edad, "años, y mi nivel educatido es", director1.nivel)

    else:
        print(MENSAJE_ERROR)

    _menuIngreso = int(input("""
    Ingrese el tipo de informacion que desea visualizar:
    1- ESTUDIANTES
    2- PROFESORES
    3- DIRECTOR
    4- Salir \n
    """))

print(MENSAJE_SALIDA)