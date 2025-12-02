# Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
aleatorio=random.randint(1,5)
print(aleatorio)
numero=int(input("introduce un numero: "))
while 1<=numero<=5:
    if numero==aleatorio:
        print("numero acertado")
    else:
        print("numero no acertado")
        numero=int(input("introduce un numero: "))
print("elnumero no esta en el rango permitido")