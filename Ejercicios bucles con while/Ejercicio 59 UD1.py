# Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.
import random
ramdom= random.randint(0,1000)
print(ramdom)
contador=0
true=False
numero=int(input("introduce un número: "))
while 0<=numero<=1000 or true!=True:
    contador+=1
    if numero<ramdom:
        print("El número que has introducido es menor")
        numero=int(input("introduce un número: "))
    if numero>ramdom:
        print("El número que has introducido es mayor")
        numero=int(input("introduce un número: "))
    else:
        print("Acertaste, has realizado", contador, "intentos")
        true=True