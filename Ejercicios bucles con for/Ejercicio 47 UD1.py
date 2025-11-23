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
    for i in range(repeticiones+1):
        numero2-=1
        numeros =numero2 + "-"
    print(numeros)



