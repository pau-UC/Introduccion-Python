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