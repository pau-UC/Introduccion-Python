# Realiza la VERSIÓN 2 de la actividad Password utilizando bucles (for).
print("INSTRUCCIONES")
print("1. Tendras que introducir como minimo 3 numeros, 3 letras y 2 simbolos")
print("2. Dentro del grupo de las letras has de escribir como minimo una mayuscula y dos minusculas")
print("2. Dentro del grupo de los numeros has de escribir como minimo dos numeros entre 1 y 5 y un numero entre 7 y 9")
print("2. Introducir un total de 3 passwords, luego el programa le indicara si son correctas o incorrectas")
print("3. Bucle que recorra el password y realice las comprobaciones y los contajes necesario.")
print("4. Testeo de 10 pruebas que permita la evaluación del código")
contador=0
while contador<=3:
    password=input("introduce el password")
    for i in password:
        if password[i].isnumeric():
            numero+=1
        elif password[i].isalpha():
            letra+=1
            if password[i].islower():
                minuscula+=1
            if password[i].isupper():
                mayuscula+=1
        else:
            simbolos+=1
    if numero>=3: