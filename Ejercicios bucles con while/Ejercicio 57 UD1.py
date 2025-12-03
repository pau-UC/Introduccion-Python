# Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
aleatorio=random.randint(1,5)
numero=0
numero=int(input("introduce un numero: "))
comprobador=numero
while 1<=numero<=5:
    if numero==aleatorio:
        print("numero acertado")
        numero+=100
    else:
        print("numero no acertado")
        numero+=100
if comprobador<1 or comprobador>5:
    print("el numero no esta en el rango permitido")