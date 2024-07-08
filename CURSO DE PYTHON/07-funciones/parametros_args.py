#Podemos definir funciones cuyo número de argumentos es variable. 
#Es decir, podemos definir funciones genéricas que no aceptan un número determinado de parámetros, 
#sino que se “adaptan” al número de argumentos con los que son llamados.

#Utilizando el operador '*' como argumento (*args)

def suma (nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
    
resultado = suma("Uriel",4,5,6,7)
print(resultado)    