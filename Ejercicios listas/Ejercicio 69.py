# Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.
repeticiones=int(input("introduce cuantos numeros quieres introducir: "))
lista=[]
listafinal=[]
for i in range(repeticiones):
    numero=int(input("introduce un numero: "))
    lista.append(numero)
lista.sort()
print(lista)
