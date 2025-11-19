# Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
notas=float(input("introduce el número de notas: "))
for j in range(notas):
    nota=float(input("introduce la nota: "))
    if nota>=5:
        print("asignatura aprobada")
    else:
        print("asignatura suspendida")
