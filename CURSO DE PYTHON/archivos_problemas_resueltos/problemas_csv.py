#Cambiar el tipo de dato de una columna
import pandas as pd

df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")

#Convertir a string los datos de una columna
df['Edad'] = df['Edad'].astype(str)


#mostrar el tipo de dato del primer elemento d ela columna edad
print(type(df['Edad'][0]))

#Reemplazando los datos de "Santarelli" por "Maestro"
df['Apellido'].replace("Santarelli","Maestro", inplace=True)
print(df['Apellido'])