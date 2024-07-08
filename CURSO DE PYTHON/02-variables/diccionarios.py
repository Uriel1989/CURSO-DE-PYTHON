#creando diccionario con dict()

diccionario =dict(nombre="uriel", apellido="santarelli")

#creando diccionario con fromkeys() valor por defecto: none
diccionario=dict.fromkeys(["nombre", "apellido"])

#creando diccionario con fromkeys() valor por defecto: "que se yo"
diccionario=dict.fromkeys(["nombre", "apellido"], "que se yo")

print(diccionario)
