import pandas as pd

#usando la funcion read_csv para leer el archivo csv
#cambiando los titulos del listado
#df = pd.read_csv("archivos\\datos.csv", names=["name","lastname","age"])

df = pd.read_csv("archivos\\datos.csv")

#obteniendo los dato de la columna nombre
#nombres =df["name"]


#Ordenamos los valores por edad 
#def_ordenado = df.sort_values("Edad")

#Ordenamos los valores por edad descendente
def_ordenado = df.sort_values("Edad", ascending=False)

#accediendo a la cantiad de filas y columnas con shape
filas_y_columnas_totales =df.shape

#obteniendo data estadistica del dataframe:
df_info =df.describe()

#CON ESTO DETERMINAMOS UN CIERTO RANGO DE POSICIONES EN LOS CARACTERES 
#EMPIEZA EN EL CARACTER '2' Y TERMINA EN LA POSICION '7'
cadena ="0123456789"
print(cadena[2:7])

#accediendo a todas las filas de una columna
#ACA ESTAMOS DETERMINANDO QUE NOS MUESTRE TODOS Y UNICAMENTE LOS APILLDOS, EL '1' ES LA POSICION DE APELLIDOS 
appelidos=df.iloc[:,1]

print(appelidos)