valor=100
while valor>150 or valor<50:
    numero=int(input("introduce un numero"))
    if numero%2==0:
        par=valor/2
        if numero%3==0:
            valor=valor-5
            print(valor)
            print("continua")
        else:
            print(valor)
            print("continua")
    else:
        impar=valor+numero
        if numero%3==0:
            valor=valor-5
            print(valor)
            print("continua")
    print(valor)
    print("continua")
if valor>150:
    print("termina(valor > 150)")
else:
    print("termina(valor < 50)")