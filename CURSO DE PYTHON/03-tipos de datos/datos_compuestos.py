#FORMATO DE LISTAS:
edad=34
altura=1.83
listas=["uriel santarelli", edad, altura]
print( listas[0])
#LAS LISTAS SE PUEDEN MODIFCAR:
listas[0]="guillermo santarelli"
print(listas[0])

#las TUPLAS NO se pueden modificar:
tupla =("uriel santarelli", edad, altura)

#CREADON CONJUNTO (SET) NO SE PUEDEN REPETIR ELEMENTOS, SU ORDEN ES ALEATORIO Y NO SE PUEDEN VER LOS ELEMENTOS 
#DE ACUERDO A SU POSICION
conjunto={"uriel", True, 45,"uriel"}
print(conjunto)

#CREANDO DICCIONARIO (DIC): CON ESTO ESTAMOS DEFINIENDO LA MANERA DE INVOCAR A LOS VALORES INGRESADOS
#LA ESTRUCTURA IMPLICA DEFINIR UNA CLAVE Y ASIGNARLE UN VALOR, EN ESTE CASO 'NOMBRE' Y EL VALOR "URIEL"

diccionario={
    'nombre':"uriel",
     'apellido':"santarelli"
}

print(diccionario ["nombre"])