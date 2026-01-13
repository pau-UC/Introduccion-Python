# Realiza la VERSIÓN 2 de la actividad Password utilizando bucles (for).
print("INSTRUCCIONES")
print("1. Tendras que introducir como minimo 3 numeros, 3 letras y 2 simbolos")
print("2. Dentro del grupo de las letras has de escribir como minimo una mayuscula y dos minusculas")
print("2. Dentro del grupo de los numeros has de escribir como mínimo un número entre 1 y 4 y dos números entre 5 y 9")
print("2. Introducir un total de 3 passwords, luego el programa le indicara si son correctas o incorrectas")
print("3. Bucle que recorra el password y realice las comprobaciones y los contajes necesario.")
print("4. Testeo de 10 pruebas que permita la evaluación del código")
contador=0
correctas=0
incorrectas=0
while contador<3:
    numero=0
    Num_opcionA=0
    Num_opcionB=0
    letra=0
    minusculas=0
    mayuscula=0
    simbolos=0
    password=input("introduce el password: ")
    comprobador=True
    contador+=1
    for i in range(len(password)):
        # Comprobar que es numerico
        if password[i].isnumeric():
            numero+=1
            if int(password[i])>=1 and int(password[i])<=4:
                Num_opcionA+=1
            elif int(password[i])>=5 and int(password[i])<=9:
                Num_opcionB+=1
            else:
                comprobador=False
        # Comprobar que es una letra
        elif password[i].isalpha():
            letra+=1
            if password[i].islower():
                minusculas+=1
            if password[i].isupper():
                mayuscula+=1
        # Si no cumple las conciones es un simbolo
        else:
            simbolos+=1
    # Comprobar que se han respetado las condiciones de la introducción.
    if numero<3:
        comprobador=False
    if letra<3:
        comprobador=False
    if minusculas<2:
        comprobador=False
    if mayuscula<1:
        comprobador=False
    if simbolos<2:
        comprobador=False
    if Num_opcionA<1:
        comprobador=False
    if Num_opcionB<2:
        comprobador=False
    # Si se han cumplido las condiciones de la introducción la contraseña es correcta.
    if comprobador==True:
        print("Contraseña", contador, "es correcta")
        correctas+=1
    # Si no se cumple, la contraseña es incorrecta.
    else:
        print("Contraseña", contador, "es incorrecta")
        incorrectas+=1
    print(numero, letra, minusculas, mayuscula, simbolos, Num_opcionA, Num_opcionB,)
print("El número de contraseñas correctas es", correctas)
print("El número de contraseñas incorrectas es", incorrectas)
# Testeo de contraseñas: Ddd791(), 7A$cñ9=2, 477Dss|@, 888jkL4, 892Sgh%&, 789Opl"·, &/238Pol), ?¿781Sdf, 23489SSff·$, 238+çñD-