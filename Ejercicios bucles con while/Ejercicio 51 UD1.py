# A partir del programa anterior, modifica el código para que sea el usuario quién introduzca el número de veces que desea que repita la frase Buenos días. Con While
contador=0
repeticiones=int(input("introduce el numero de veces que deseas repetir la frase: "))
while contador<repeticiones:
    contador+=1
    print("buenos dias")