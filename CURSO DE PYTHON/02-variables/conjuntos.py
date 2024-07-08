#creando conjuntos con set()

conjunto =set (["dato01"])


#No se puede poner un conjunto dentro de otro de esta manera
#conjunto2={conjunto,"dato3"}

#este conjunto es inmutable y es asi como debe anidarse un conjunto dentro de otro
conjunto1=frozenset(["dato01","dato02"])
conjunto2={conjunto1,"datos3"}

#print(conjunto2)

#teoria de conjuntos

conjunto3 ={1,2,3,4,5}
conjunto4={1,2,3}

#verificando su es un conjunto
resultado1 = conjunto4.issubset(conjunto3)
#devuelve true porque efectivamente el cojunto 3 engloba al conjunto 4
#print(resultado1)

#verificar si 2 conjuntos son distintos

conjunto5={6,7,9}
conjunto6={1,2,3}

resultado2=conjunto6.isdisjoint(conjunto5)

#devuelve true porque efectivametne son distintos, si hay por lo menos 1 elemento de los conjuntos en comun devolvera false
print(resultado2)