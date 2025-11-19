# Programa que sume los n primeros números naturales. n Lo introduce el usuario. 
suma=0
número=int(input("introduce un número: "))
for i in range (1, número+1):
    suma+= i
print("La suma total de números naturales es:", suma )
