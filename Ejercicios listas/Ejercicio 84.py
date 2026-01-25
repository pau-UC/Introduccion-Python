import random
lista1=["casa","barco","gato","perro","madera","agua","pantalón"]
aleatorio= random.randint(0,6)
adivinar=lista1[aleatorio]
letras = list(adivinar)
random.shuffle(letras)
palabradesordenada="".join(letras)
intentos=0
print(palabradesordenada)
while not intentos>=3:
    palabra=input("introduce la palabra que crees que es: ")
    if palabra==adivinar:
        print("Acertaste")
        intentos=1000
    else:
        print("No has acertado")
        intentos+=1