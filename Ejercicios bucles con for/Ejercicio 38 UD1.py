# A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10 
notas=int(input("introduce el número de notas: "))
for j in range(notas):
    nota=float(input("introduce la nota: "))
    if nota>=0 and nota<=10:
        if nota>=5:
            print("asignatura aprobada")
        else:
            print("asignatura suspendida")
    else:
        print("Has introducido una nota equivocada")