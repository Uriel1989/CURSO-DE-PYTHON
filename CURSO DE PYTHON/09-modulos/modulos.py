#IMPORTAMOS EL MODULO 
import modulos.funciones_buenas.saludar as bienvenida #LE OTORGAMOS UN NOMBRE

saludo=bienvenida.saludar("Uriel")

print(saludo)

#IMPORTAMOS 2 FUNCIONES 
from modulos.funciones_buenas.saludar import saludar, saludar_alternativa

#CREAMOS LAS VARIABLES CON LOS SALUDOS
saludo=bienvenida.saludar("Uriel")
saludar_alter=saludar_alternativa("Guillermo")

#MOSTRAMOS LOS RESULTADOS
print(saludo)
print(saludar_alter)

