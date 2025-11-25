longitud=int(input("introduce la cantidad de cifras: "))
numero=int(input("introduce un número con la misma cantidad de cifras: "))
pares=0
producto=0
if longitud==len(str(numero)):
    for i in range(longitud):
        producto*=str(numero[i])
        if numero[i]%2==0:
            pares+=1
else:
    print("Longitud incorrecta")
print("Producto de cifras:", producto)
print("cifras pares:", pares)