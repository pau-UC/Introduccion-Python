longitud=int(input("introduce la cantidad de cifras: "))
numero=int(input("introduce un número con la misma cantidad de cifras: "))
pares=0
producto=1
if longitud==len(str(numero)):
    for i in str(numero):
        producto=producto * int(i)
        if int(i)%2==0:
            pares+=1
    print("Producto de cifras:", producto)
    print("cifras pares:", pares)
else:
    print("Longitud incorrecta")