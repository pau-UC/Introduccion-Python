# Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
repetir=""
comprobador=False
while not repetir== "n" and comprobador==False:
    numero1=int(input("introduce el primer numero: "))
    numero2=int(input("introduce el segundo numero:"))
    suma=numero1+numero2
    print("El resultado de la suma es:", suma)
    repetir=input("deseas repetir la operacion s/n: ")
    if repetir=="s":
        comprobador=True
print("programa finalizado")
# Esta mal