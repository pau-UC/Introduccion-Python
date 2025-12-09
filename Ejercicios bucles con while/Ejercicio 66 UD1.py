#  Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo se comporta el dado en lanzamientos producidos durante aprox 3 segundos.
import random
import time 
contador=0
uno=0
dos=0
tres=0
cuatro=0
cinco=0
seis=0
inicio=time.time()
while time.time()-inicio<3:
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