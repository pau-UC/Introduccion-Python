positivos=0
negativos=0
mayores=0
for i in range(7):
    numero=int(input("introduce un número: "))
    if numero>=0:
        positivos+=numero
        if numero>100:
            mayores+=1
    elif numero<0:
        negativos+=numero
print("Suma positivos:", positivos)
print("Suma negativos:", negativos)
print("Mayores de 100:", mayores)