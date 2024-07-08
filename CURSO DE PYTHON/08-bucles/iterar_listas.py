animales = ["perro", "gato", "loro", "tortuga"]

#recorriendo el ciclo for
for animal in animales:
    print(f'La variable en esta instancia del ciclo es: {animal}')

#recoriendo la lsta de numers y multiplicando cada valor por 10

numeros =[52,16,14,72]

for numero in numeros:
    resultado = numero * 10
    print(f'El resultado de la multiplicacion es: {resultado}')

#aca estamos recorriendo 2 listados al mismo tiempo
for numero, animal in zip(animales, numeros):
    print(f'recorriendo lista 1: {numero}')
    print(f'recorriendo lista 2: {animal}')

#recorriendo un rango, que conste que NO mostrara el 10 ni el 20
for num in range(10,20):
    print(num)
    
#usando el else
for numero in numeros:
    print(f'ejecuntando el ultimoblucle, valor actual: {numero}')
else:
    print("El bucle termino")