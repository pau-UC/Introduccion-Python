# Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo
repeticiones=int(input("introduce la cantidad de palabra: "))
lista=[]
lista2=[]
for i in range(repeticiones):
    palabra=input("introduce una palabra: ")
    lista.append(palabra)
    lista2.append(palabra)
lista.sort()
lista2.sort()
lista2.reverse()
print("lista 1 contiene", lista)
print("Lista 2 contiene", lista2)