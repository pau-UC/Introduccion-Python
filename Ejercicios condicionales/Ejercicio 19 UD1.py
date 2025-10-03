# Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales.
var1=float(input("introduce un número por favor: "))
var2=float(input("introduce otro número por favor: "))
if var1>var2:
    print("el número", var1, "es mayor que el número", var2)
elif var1<var2:
    print("el número", var2, "es mayor que el número", var1)
else:
    print("Ambos números son iguales")