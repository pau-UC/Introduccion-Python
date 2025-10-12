
letra=input("introduce la letra por favor: ")
if letra.isalpha()==True:
    if letra.islower()==True:
        print("la letra es minúscula: ")
    elif letra.isupper()==True:
        print("la letra es mayúscula: ")
elif letra.isnumeric()==True:
    print("el valor introducido es un número")
else:
    print("La letra es un simbolo")