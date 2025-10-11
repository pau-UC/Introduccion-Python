# Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
letra=input("introduce la letra por favor: ")
if letra.isalpha()==True:
    if letra.islower()==True:
        print("la letra es minúscula: ")
    elif letra.isupper()==True:
        print("la letra es mayúscula: ")
else:
    print("La letra es mayúscula ¿?")