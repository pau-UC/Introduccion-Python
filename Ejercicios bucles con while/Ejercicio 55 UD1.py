#  Última vez que reutilizamos el mismo código.. lo prometo       . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While 
repeticiones=0
sumafinal=0
while sumafinal<=50:
    repeticiones+=1
    numero1=int(input("introduce el primer numero: "))
    numero2=int(input("introduce el segundo numero: "))
    suma=numero1+numero2
    print("El resultado de la suma es:", suma)
    sumafinal+=suma
    if repeticiones>1:
        print("El total acumulado es:", sumafinal, "y llevas", repeticiones, "operaciónes realizadas")
    else:
        print("El total acumulado es:", sumafinal, "y llevas", repeticiones, "operación realizada")
    if sumafinal%2==0:
        break
print("Fin del Programa")