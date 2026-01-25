# Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra
lista1=["casa","barco","gato","perro","madera","agua","pantalón"]
import random
aleatorio= random.randint(0,6)
adivinar=lista1[aleatorio]
acertar=0
print(adivinar)
while not acertar==1:
    palabra=input("introduce la palabra secreta: ")
    if palabra==adivinar:
        print("Acertaste")
        acertar=1
    else:
        print("Has fallado, sigue jugando")
