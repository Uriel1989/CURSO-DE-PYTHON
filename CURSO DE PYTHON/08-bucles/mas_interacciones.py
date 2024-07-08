frutas =["manzanas", "pera", "uvas", "durazno", "banana"]
comidas =["manzanas", "pera", "uvas", "durazno", "banana"]

#Estamos estableciendo que cuando la variable tenga valor "banana", se la saltea y sigue de largo
#NO LO VA MOSTRAR
for fruta in frutas:
    if fruta =='banana':
       continue
    print(f'Me voy a comer una {fruta}')
    

    