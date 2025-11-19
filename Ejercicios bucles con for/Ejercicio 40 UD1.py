# Crea un programa que cuente todos los números pares hasta el número 50
numero=0
impar=0
par=0
for i in range(50):
    numero+=1
    if numero%2==0:
        par+=1
    else:
        impar+=1
print("el total de pares:", par)
print("el total de impares:", impar)