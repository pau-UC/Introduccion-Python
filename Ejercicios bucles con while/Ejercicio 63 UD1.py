#  Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número de veces que se repite cada número.
import random
contador=0
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0
while contador!=100:
    contador+=1
    aleatorio=random.randint(1,6)
    if aleatorio==1:
        uno+=1
    if aleatorio==2:
        dos+=1
    if aleatorio==3:
        tres+=1
    if aleatorio==4:
        cuatro+=1
    if aleatorio==5:
        cinco+=1
    if aleatorio==6:
        seis+=1
print("Uno:", uno)
print("dos:", dos)
print("Tres:", tres)
print("Cuatro:", cuatro)
print("Cinco:", cinco)
print("Seis", seis)