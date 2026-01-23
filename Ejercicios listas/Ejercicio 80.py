# Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
numero=input("introduce un número entero o decimal: ")
if numero.isalpha():
    print("El numero no es un decimal")
elif float(numero) % 1!=0:
    print("El número es decimal")
else:
    print("El numero no es un decimal")