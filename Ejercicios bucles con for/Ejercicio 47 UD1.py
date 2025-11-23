# Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso.
numero1=int(input("introduce el primer intervalo: "))
numero2=int(input("introduce el segundo intervalo: "))
if numero1>numero2:
    print(numero1,"-")
    repeticiones=numero1-numero2
    for i in range(repeticiones):
        numero1-=1
        print(numero1,"-")
elif numero2>numero1:
    print(numero2,"-")
    repeticiones=numero2-numero1
    for i in range(repeticiones):
        numero2-=1
        print(numero2,"-")


