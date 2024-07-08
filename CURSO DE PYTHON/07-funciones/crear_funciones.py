#Creando funciones simples
def saludar():
    print("Hola Uriel, buen dia, me alegra que estes estudiando/practicando")
saludar()

#Creando una funcion con parametros

def saludo(nombre):
    print(f'Hola {nombre}, como estas?')
    
saludo("Uriel")

#Crear una funcion que nos retorne valores
#En este programa nos va a devolver una contraseña aleatoria
def crear_contraseña_random(num):
    chars = "engeng" #creacion de caracteres aleatorios
    num_entero=str(num) #converitr a string el primer numero
    num=int(num_entero[0]) #obtengo el primero valor
    c1=num - 2 #al valor ingresado se le restara 2
    c2=num     #se deja el valor ingresado
    c3=num - 5 #se le resta 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}" #aqui se determinan las posiciones de los
                                                             #caracteres y se multiplica el valor num
    return contraseña
    
password= crear_contraseña_random(50)
frase= f"Tu contraseña nueva es: {password}"
print(frase)