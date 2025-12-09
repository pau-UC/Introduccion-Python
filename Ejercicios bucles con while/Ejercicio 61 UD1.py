# A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.
numero=int(input("introduce el numero: "))
contador=0
while contador!=10:
    contador+=1
    producto= numero*contador
    print(producto)
    if producto>=40:
        break
print("Fin del Programa")