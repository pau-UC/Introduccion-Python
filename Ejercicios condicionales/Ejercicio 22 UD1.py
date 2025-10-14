# Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
nota=float(input("introduce tu nota: "))
if nota<=10 and nota>=0: 
    if nota>=5:
        print("has sacado un", nota, "y has aprobado")
    elif nota<5:
        print("has sacado un", nota, "y has suspendido")
else:
    print("la nota que has sacado no esta entre 0 y 10")