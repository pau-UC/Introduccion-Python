import random

num_secreto=random.randint(1, 20)
print(num_secreto)
numero=int(input("introduce un número del 1 al 20: "))
while num_secreto!=numero:
    if numero>0 and numero<=20:
        print(f"has introducido el numero {numero}, y no has acertado")
    else:
        print("rango incorrecto")
    numero=int(input("introduce un número del 1 al 20: "))

print("acertaste")
