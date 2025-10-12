
nota=float(input("introduce tu nota: "))
if nota<=10 and nota>=0: 
    if nota>=5:
        print("has sacado un", nota, "y has aprobado")
    elif nota<5:
        print("has sacado un", nota, "y has suspendido")
else:
    print("la nota que has sacado no esta entre 0 y 10")