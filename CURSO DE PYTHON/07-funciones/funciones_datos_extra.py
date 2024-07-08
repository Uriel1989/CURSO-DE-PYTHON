#El orden de los parametros es importante

def frase (nombre, apellido, adjetivo):
    
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante =frase("Uriel", "Santarelli", "crack")

print (frase_resultante)