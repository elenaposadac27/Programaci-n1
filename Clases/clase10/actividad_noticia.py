archivo = open("noticia.txt")
import funciones_lectura_archivos as helper

lineas = helper.leer_archivo("noticia.txt")
helper.mostrar_lineas(lineas)

Opinion = ["MI OPINION ES LA SIGUIENTE (ESCRIBIR OPINION)"]
helper.escritura_archivo("Opinion.txt", Opinion)
