# La letra de tu DNI no está puesta al azar, se obtiene de dividir el número entre 23. El resto de esta operación está entre los valores del 0 y 22, asociándose a una letra de la siguiente tabla.
# Diseñar un programa que al introducir un número  calcule la letra correspondiente del DNI teniendo en cuenta las instrucciones
resto=0
Lista_intentos=[]
letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
repetir="s"
longitud=0
numerico=0
dni_correctos=[]
dni_incorrectos=[]
while repetir !="n":
    dni=input("Introduce los números del DNI: ")
    if len(dni)==8:
        if dni.isnumeric():
            resto=int(dni)%23
            for i in range(len(letras)):
                if letras[i]==letras[resto]:
                    dni+= "-" + letras[i]
                    Lista_intentos.append(3)
                    dni_correctos.append(dni)
        else:
            print("El valor introducido debe ser numerico")
            Lista_intentos.append(1)
            numerico+=1
            dni_incorrectos.append(dni)     
        repetir=input("Deseas introducir otro DNI s/n: ")
    else:
        print("El valor introducido no cumple con la longitud correcta")
        repetir=input("Deseas introducir otro DNI s/n: ")
        Lista_intentos.append(0)
        longitud+=1
        dni_incorrectos.append(dni)
errorres=len(dni_incorrectos)
aciertos=len(dni_correctos)
print("1. Listar DNI correcto de menor a mayor")
print("2. Listar DNI incorrecto de menor a mayor")
print("3. Numero total de errores producidos")
print("4. Numero total de DNI correctos")
print("5. Porcentajes intentos con error y sin error")
print("6. Salir s/n")
numero=int(input("Introduce que opción elige: "))
if numero==1:
    dni_correctos.sort()
    print(dni_correctos)
if numero==2:
    dni_incorrectos.sort()
    print(dni_incorrectos)
if numero==3:
    print(errorres)
if numero==4:
    print(aciertos)
if numero==5:
    intentos=errorres+aciertos
    correctos=aciertos/intentos*100
    incorrectos=errorres/intentos*100
    longitudes=longitud/intentos*100
    numericos=numerico/intentos*100
    print("El número de intentos és:", intentos)
    print("El porcentaje de DNI correctos son:", correctos)
    print("El porcentaje de DNI incorrectos son:", incorrectos)
    print("El porcentaje de DNI con error de longitud es:", longitudes)
    print("El porcentaje de DNI con error de dígitos es:", numericos)
if numero==6:
    print("Programa finalizado")