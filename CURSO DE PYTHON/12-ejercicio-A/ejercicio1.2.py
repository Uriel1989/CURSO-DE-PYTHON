#CALCULA EL TIEMPO QUE TE TARDAS AL HABLAR

frase =input("decime una frase y te calculo cuanto tardas en pronunciarla: ")

#la funcion split nos permite separar las palabras, caso contrario el programa va a contar los espacios vacios entre palabras
palabras_separadas =frase.split(" ")
cantidad_de_palabras =len(palabras_separadas)

print(f'Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/2} segundos en decirlo')