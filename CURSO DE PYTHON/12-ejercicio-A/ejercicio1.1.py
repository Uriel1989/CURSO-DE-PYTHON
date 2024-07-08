#SE CALCULA EL TIEMPO EN COMPARACION A OTROS CURSOS

#promedio de duracion:
otros_cursos_min = 2.5
otros_cursos_max =7
otros_cursos_promedio =4
uriel_curso=1.5

#diferencias de duracion
diferencia_con_min =100-(uriel_curso/otros_cursos_min*100)
diferencia_con_max =100-(uriel_curso*1000//otros_cursos_max/10)
diferencia_con_promedio =100-(uriel_curso/otros_cursos_min*100)


print(f'El curso de uriel dura un {diferencia_con_min} % menos que el mas rapido')
print(f'El curso de uriel dura un {diferencia_con_max} % menos que el mas lento')
print(f'El curso de uriel dura un {diferencia_con_promedio} % menos que el promedio')