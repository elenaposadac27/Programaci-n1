import matplotlib.pyplot as plt

#sizes son los porcentajes, deben sumar 100%
#explode es como la elevacion que se le da a ese fragmento, en este caso el fragmento de "JAVA" aparecera sobresalido en el gráfico
labels = 'Java', 'python', 'C#', 'JavaScript'
sizes = [15, 45, 30, 10]
explode = (0.1, 0, 0, 0)

#shadow permite agregar sombra al grafico, para hacerlo se pone True
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("LENGUAJES DE PROGRAMACIÓN MAS USADOS")
plt.savefig("Grafico_pie.png")
plt.show()

