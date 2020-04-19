import funciones_lectura_archivos as helper
#Leimos el archivo completo
lineas= helper.leer_archivo("libro.txt")

#Lo mostramos linea por linea
helper.mostrar_lineas(lineas)

#crear un nuevo archivo con contenido
Texto = ["Hola este es mi primer archivo creado en python \n","Espero que funcione!!"]
helper.escritura_archivo("Intento1.txt", Texto)

#editar un archivo ya existente
helper.agregar_linea("libro.txt", "\nAutor: Rene Descartes")