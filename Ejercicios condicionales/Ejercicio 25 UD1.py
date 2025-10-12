# Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota=float(input("introduce tu nota: "))
if nota<=10 and nota>=0: 
    if nota>=8.5:
        print("tu nota es un", nota, "y has sacado un excelente")
    elif nota>=6.5 and nota<8.5:
        print("tu nota es un", nota, "y has sacado un notable")
    elif nota>=5 and nota<6.5:
        print("tu nota es un", nota, "y has sacado un satisfactorio")
    elif nota<5:
        print("tu nota es un", nota, "y has sacado un insufucuente")
else:
    print("la nota que has sacado no esta entre 0 y 10")