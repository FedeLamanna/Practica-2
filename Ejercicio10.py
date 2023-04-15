nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

#A
def crear_dicc(nombres, notas_1, notas_2):
    for nombres, nota_1, nota_2 in zip(nombres, notas_1, notas_2):
        dic_estudiantes[nombres] = [nota_1, nota_2]
    return dic_estudiantes

#B
def promedio(dic_estudiantes):
    for nombre in dic_estudiantes:
        dic_promedio_por_alumno[nombre] = 0 if len(dic_estudiantes) == 0 else sum(dic_estudiantes[nombre]) / len(dic_estudiantes[nombre])
    return dic_promedio_por_alumno

#C
def promedio_general(dic_promedio_por_alumno):
    return (0 if len(dic_promedio_por_alumno) == 0 else (sum(dic_promedio_por_alumno.values()) / len(dic_promedio_por_alumno)))
    
#D    
def promedio_mas_alto(dic_promedio_por_alumno):
    return max(dic_promedio_por_alumno.items(), key=lambda x:x[1])[0]

#E
def nota_mas_baja(dic_estudiantes):
    return min(dic_estudiantes.items(), key=lambda x: min(x[1]))[0] #Hay que comparar el minimo en nota_1 y nota_2

    

n1=nombres.replace("\n","")
n1=n1.replace(","," ")
nomb=n1.split(" ")
while "" in nomb:
    nomb.remove('')

dic_estudiantes = {}
dic_estudiantes = crear_dicc(nomb, notas_1, notas_2) #Punto A - Creacion del diccionario
print(dic_estudiantes)

dic_promedio_por_alumno = {}
dic_promedio_por_alumno = promedio(dic_estudiantes) #Punto B - Promedio por alumno
print(dic_promedio_por_alumno)

print(f"El promedio general del curso es {promedio_general(dic_promedio_por_alumno)}") #Punto C - Promedio general

print(f"El alumno con el promedio mas alto es {promedio_mas_alto(dic_promedio_por_alumno)}") #Punto D - Alumno con promedio mas alto

print(f"El alumno con la nota mas baja es {nota_mas_baja(dic_estudiantes)}") #Punto E - Alumno con la nota mas baja


