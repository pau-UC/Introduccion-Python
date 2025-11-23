
palabra=input("introduce la palabra secreta: ")
for i in range(len(palabra)):
    letra=input("introduce la letra: ")
    if letra in palabra:
        print("la letra se encuentra en la posición", i+1)
    else:
        print("la letra no existe")