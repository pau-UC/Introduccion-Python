# Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.
letra=input("introduce la letra por favor: ")
if letra.isalpha()==True:
    if letra.islower()==True:
        print("la letra es minúscula: ")
    elif letra.isupper()==True:
        print("la letra es mayúscula: ")
elif letra.isnumeric()==True:
    print("el valor introducido es un número")
else:
    print("El valor introducido es un símbolo")