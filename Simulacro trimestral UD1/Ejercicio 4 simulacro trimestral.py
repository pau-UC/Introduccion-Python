valor=100
numero=int(input("introduce un numero: "))
while 50<=valor<=150:
    if numero%2==0:
        valor=valor/2
    else:
        valor=valor+numero
    if numero%3==0:
        valor=valor-5
    print(valor)
    if 50<=valor<=150:
        numero=int(input("introduce un numero: "))