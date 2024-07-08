import pandas as pd

#Matplotlib es una biblioteca para la generación de gráficos en dos dimensiones, 
#a partir de datos contenidos en listas o arrays en el lenguaje de programación Python.
import matplotlib.pyplot as plt

#Seaborn es una biblioteca para crear gráficos estadísticos en Python. 
#Está basada en Matplotlib, y se integra con las estructuras de Pandas. 
#Esta biblioteca es tan potente como Matplotlib, 
#pero aporta simplicidad y funciones inéditas. Permite explorar y comprender rápidamente los datos.
import seaborn as sns

df=pd.read_csv("archivos_problemas_graficos\\pedos.csv")

#creando el grafico
sns.lineplot(x="fechas",y="pedos",data=df)

#creando un punto en el momento de mas pedos
plt.plot("01-09",17,"o")

#mostrando el grafico
plt.show()