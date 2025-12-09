concatenarpar=""
concatenarimpar=""
numero1=int(input("introduce un numero: "))
numero2=int(input("introduce otro numero: "))
for i in range(numero1,numero2+1):
    if i %2==0:
        concatenarpar=concatenarpar + str(i) + "-"
    if not i%2==0:
        concatenarimpar=concatenarimpar + str(i) + "-"
print("los numeros pares son:", concatenarpar[:-1])
print("los numeros impares son:", concatenarimpar[:-1])