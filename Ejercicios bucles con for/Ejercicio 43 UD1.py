# Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima por pantalla cada letra
palabra=input("introduce la palabra: ")
longitud=len(palabra)
for i in range(longitud):
    print("En la posición", i, "está la", palabra[i])