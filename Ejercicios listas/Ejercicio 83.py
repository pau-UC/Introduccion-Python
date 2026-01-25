# Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así sucesivamente. 
lista1=["casa","barco","gato","perro","madera","agua","pantalón"]
import random
aleatorio= random.randint(0,6)
adivinar=lista1[aleatorio]
repetir="s"
puntos=8
listapuntos=[]
while not repetir=="n":
    palabra=input("introduce la palabra secreta: ")
    if palabra==adivinar:
        print("Acertaste")
        listapuntos.append(puntos)
        puntos=8
        aleatorio= random.randint(0,6)
        adivinar=lista1[aleatorio]
        repetir=input("Deseas introducir otro alumno s/n: ")
    else:
        print("Has fallado, sigue jugando")
        puntos-=1
print(listapuntos)
listamedia=sum(listapuntos)/len(listapuntos)
print(listamedia)