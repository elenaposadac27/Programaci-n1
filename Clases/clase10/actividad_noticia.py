import funciones_lectura_archivos as helper
archivo = open("noticia.txt",'r')

lineas= helper.leer_archivo("noticia.txt")
helper.mostrar_lineas(lineas)
