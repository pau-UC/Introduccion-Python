# Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
aleatorio=random.randint(1,5)
numero=0
contador=0
while contador<3:
    numero=int(input("introduce un numero: "))
    contador+=1
    if numero==aleatorio:
        print("numero acertado")
        break
    else:
        print("numero no acertado")
if numero<1 or numero>5:
    print("el numero no esta en el rango permitido")