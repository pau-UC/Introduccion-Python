# Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
frase= "A quién madruga Dios ayuda"
frase2= "a Quien Madruga dios Ayuda"
palabra=input("introduce una palabra de la frase: ")
índice= frase.find(palabra) and frase2.find(palabra)
if índice>=0:
    print("La palabra está en la frase y está en el índice", índice)
else:
    print("La palabra no está en la frase")