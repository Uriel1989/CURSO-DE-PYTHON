#Encontrando el numero mayor de una lista

numeros={4,7,42,15}

numero_mas_alto = max(numeros)
print(f'El numero mas alto es: {numero_mas_alto}')

#Encontrando el numero menor de una lista

numeros={4,7,42,15}

numero_mas_bajo = min(numeros)
print(f'El numero mas bajo es: {numero_mas_bajo}')

#Ordenar a 6 decimales
#Con roundo y el '3' despues de la coma podemos establecer 
#cuantos decimales queremos que se muestren
numero = round(10.2132546684,3)
print(numero)

#Retoma False ->0, vacio False, ninguno
resutado_bool= bool(None)
print(resutado_bool)

#Retorna True si todos los valores son verdaderos, es decir, diferentes de 0
resultado_all = all([1,"true", [3,23]])
print(resultado_all)


