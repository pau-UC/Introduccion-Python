# A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10.
var1=float(input("introduce un número por favor: "))
var2=float(input("introduce otro número por favor: "))
if var1>=0 and var1<=10 and var2>=0 and var2<=10:
    if var1>var2:
        print("el número", var1, "es mayor que el número", var2)
    elif var1<var2:
        print("el número", var2, "es mayor que el número", var1)
    else:
        print("Ambos números son iguales")
else:
    print("Uno o los dos números están fuera de los límites establecidos")