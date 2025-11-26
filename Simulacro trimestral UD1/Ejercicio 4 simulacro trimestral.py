valor=100
numero=int(input("introduce un numero"))
while valor>=150 or valor<=50:
    if numero%2==0:
            print(valor)
        valor=valor/2
    else:
        valor=valor+numero
    if numero%3==0:
        valor=valor-5
    print(valor)
    if valor<=150 and valor>=50:
    numero=int(input("introduce un numero"))