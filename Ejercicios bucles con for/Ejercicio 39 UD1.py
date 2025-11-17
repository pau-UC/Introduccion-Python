# Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0.
positivo=0
negativos=0
cero=0
números=int(input("introduce la cantidad de números que deseas introducir: "))
for j in range(números):
    número=float(input("introduce un número: "))
    if número>0:
        positivo += 1
    elif número<0:
        negativos += 1
    else:
        cero += 1
print("La cantidad de números positivos es:", positivo)
print("La cantidad de números negativos es:", negativos)
print("La cantidad de números cero es:", cero)