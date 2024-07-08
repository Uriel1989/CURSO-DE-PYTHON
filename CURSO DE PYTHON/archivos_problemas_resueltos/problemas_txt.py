#2 listas, una con nombres y otra con apellidos
nombres= ["Uriel", "Matias", "Florencia", "Camila"]
apellidos=["Santarelli", "Braga","Whright", "Gonzales"]

#Mostrar esta informacion de forma optima en un TXT

with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellidos: {a}\n--------\n") for n, a in zip (nombres, apellidos)]
    
    