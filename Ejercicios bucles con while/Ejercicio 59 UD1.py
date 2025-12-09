# Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.
import random
ramdom= random.randint(0,1000)
print(ramdom)
intentos=0
numero=-105
while numero!=ramdom:
    intentos+=1
    numero=int(input("introduce un número: "))
    if numero > ramdom:
        print("El número que has introducido es mayor")
    elif numero < ramdom:
        print("El número que has introducido es menor ")
print("Acertaste, has realizado", intentos, "intentos")