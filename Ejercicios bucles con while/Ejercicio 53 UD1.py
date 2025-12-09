#  A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
repetir="s"
repeticiones=0
sumafinal=0
while repetir== "s":
    repeticiones+=1
    numero1=int(input("introduce el primer numero: "))
    numero2=int(input("introduce el segundo numero: "))
    suma=numero1+numero2
    print("El resultado de la suma es:", suma)
    repetir=input("deseas repetir la operacion s/n: ")
    sumafinal+=suma
print("Resumen")
print("la suma total es:", sumafinal, "y el numero de repeticiones es:", repeticiones)