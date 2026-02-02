
resto=0
Lista_intentos=[]
letras=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
repetir="s"
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
            print(dni)
            print(resto)
        else:
            print("El valor introducido debe ser numerico")
            Lista_intentos.append(1)
            dni_incorrectos.append(dni)     
        repetir=input("Deseas introducir otro alumno s/n: ")
    else:
        print("El valor introducido no cumple con la longitud correcta")
        Lista_intentos.append(0)
        dni_incorrectos.append(dni)
print(dni_correctos)
print(dni_incorrectos)
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
    errorres=len(dni_incorrectos)
    print(errorres)
if numero==4:
    aciertos=len(dni_correctos)
if numero==5:
    print("")