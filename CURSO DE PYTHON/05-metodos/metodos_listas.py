lista =list(["hola","uriel",34])

#devuevle la cantidad de elementos en la lista
resultado = len(lista)

#agregando elementos a la lista

lista.append("dato agregado")

#agregando un elementos a la lista en un indice especifico 
lista.insert(2,"insertado en el indice 2")

#agregando varios elementos a la lista
lista.extend([False,2023])

#eliminando elementos de al lista por su indice
lista.pop(1)

#removiendo un elemento por su valor
lista.remove("dato agregado")

#elimando todos los elementos de la lista
#lista.clear()

#ordena la lista de menor a mayor (unicamente valores numericos, no debe haber valores string)
#lista.sort()

#invirtiendo los elementos de una lista (unicamente valores numericos, no debe haber valores string)
#lista.reverse()

#verificando si un elementos se encuentra en la lista
elemento_encontrado = lista.index(2023)

#va a mostrar la posicion del elemento buscado
print(elemento_encontrado)

print(lista)