import funciones_lectura_archivos as helper

lineas = helper.leer_archivo("noticia.txt")
helper.mostrar_lineas(lineas)

Opinion = ["Pienso que en medio de la contingencia muchas empresas de diferentes sectores se han visto\n", 
"afectadas economicamente; ya sea debido a la imposibilidad de operacion o al decremento en sus ventas.\n", 
"Es por esto que considero que esta iniciativa por la que optó el gremio cafetero del departamento del Quindio\n",
"es una gran oportunidad, no solo para mantenerse a flote en epocas de crísis al acercarse mas a sus clientes,\n",
"sino tambien para lograr que la industria crezca pensando a futuro al lograr dar a conocer su marca.\n",
"Ademas, al mismo tiempo se esta contribuyendo a la generacion de empleo en medio de la crisis y con esto a que\n",
"las familias de los cafeteros (que en su mayoria viven del día a día) puedan recibir los ingresos de su produccion con normalidad."]
helper.escritura_archivo("Opinion.txt", Opinion)

helper.agregar_linea("noticia.txt", "\nFecha de publicacion: 19 DE ABRIL DE 2020")
helper.agregar_linea("noticia.txt", "\nPeriodico: EL TIEMPO")