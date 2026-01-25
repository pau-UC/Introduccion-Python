# A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta.  El usuario tendrá 3 oportunidades para adivinar la palabra. 
import random
lista1=["casa","barco","gato","perro","madera","agua","pantalón"]
aleatorio= random.randint(0,6)
adivinar=lista1[aleatorio]
letras = list(adivinar)
random.shuffle(letras)
palabradesordenada="".join(letras)
intentos=0
print(palabradesordenada)
while not intentos>=3:
    palabra=input("introduce la palabra que crees que es: ")
    if palabra==adivinar:
        print("Acertaste")
        intentos=1000
    else:
        print("No has acertado")
        intentos+=1