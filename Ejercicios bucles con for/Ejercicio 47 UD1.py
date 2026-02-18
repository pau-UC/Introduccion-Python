# Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso.
numero1=int(input("introduce el primer intervalo: "))
numero2=int(input("introduce el segundo intervalo: "))
numero = ""
if numero1>numero2:
    repeticiones=numero1-numero2
    for i in range(repeticiones):
        numero+= numero1 + str(i) + "-"
    print(numero)
elif numero1<numero2:
    repeticiones=numero2-numero1
    for i in range(repeticiones):
        numero+= numero1 + str(i) + "-"
    print(numero)
