#  Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural. Con While 
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
print("Fin del Programa")