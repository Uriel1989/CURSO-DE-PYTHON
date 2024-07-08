#Forma de crear una funcion anonima, es decir, 
#no tiene nombre, no esta definida, no esta asociada a NADA
numeros = [1,2,3,4,5,6,7,8,9,10]

#Este programa nos va a mostrar unicamente los numeros pares de la lista ingresada
numeros_pares=filter(lambda numero:numero%2==0, numeros)

print(list(numeros_pares))