# Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.
frase= "A quién madruga Dios ayuda"
palabra=input("introduce una palabra de la frase: ")
índice= frase.find(palabra)
if índice>=0:
    print("La palabra está en la frase y está en el índice", índice)
else:
    print("La palabra no está en la frase")