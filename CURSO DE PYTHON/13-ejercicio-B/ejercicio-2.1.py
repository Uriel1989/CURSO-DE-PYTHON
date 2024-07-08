#Falto el profesor y los alumnos van a armar la clase
#Pedir el nombre y la edad de los compañeros que viniero a la clase-

#Funcion para obtener el asistente y el profesor segun la edad
def obtener_compañeros (cantidad_de_compañeros):
    #creando la lista con los compañeros
    compañeros=[]
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre=input("Ingrese el nombre del compañero: ")
        edad = int (input("Ingrese la edad del compañero: "))
        compañero= (nombre, edad)
        
        #Agregando la informacion a la lista
        compañeros.append(compañero)
        
        #ordenando de mayor a menor segun la edad
    compañeros.sort(key=lambda x:x[1])
    
    #compañero[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
    #para definir al asistente y al profesor
    asistente =compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla
    return asistente, profesor

#desempaquetamos lo que nos retorna la funcion 
asistente, profesor=obtener_compañeros(5)

#Muestra el resultado
print(f"El profesor es: {profesor} y su asistente es {asistente}")