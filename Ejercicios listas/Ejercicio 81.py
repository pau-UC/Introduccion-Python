# A partir de una lista definida, busca el método apropiado para que se visualice un valor de la lista al azar.
lista1=["casa","barco","gato","perro","madera","agua","pantalón"]
import random
aleatorio= random.randint(0,7)
print(lista1[aleatorio])