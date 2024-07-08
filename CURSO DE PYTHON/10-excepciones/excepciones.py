

def sumar_dos():
    #utilizamos while para crear un bucle que nos permite seguir usando el programa
    while True:
        a=input("numero 1: ")
        b=input("numero 2: ")
        #con el try estamos estableciendo una excepcion en caso 
        #de que se ingresen valores erroneos
        try:
            #convertimos los valores ingresados de string a int
            resultado = int(a) + int (b)
            #con esto damos un alto a la excepcion
            break
        #con ValueError establecemos que se nos indique 
        #el tipo de error que captura la excepcion
        except ValueError as e:
            print("Por favor, no ingrese un valor distinto de un numero entero")
            print(f"ERROR: {e}")
    #mostrar el resultado        
    return resultado

print(sumar_dos())