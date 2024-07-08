diccionario ={
    "nombre":"uriel",
    "apellido": "Santarelli",
    "Edad": 34
}
#recorriendo un diccionario con items()para obtener las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value=datos[1]
    print(f'La clave es: {key} y el valor es: {value}') 