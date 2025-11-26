<<<<<<< Updated upstream
#  Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes: 
palabra=input("introduce una palabra: ")
vocales=""
consonantes=""
for i in range(len(palabra)):
    if palabra[i] in ["a", "e", "i", "o", "u"]:
        vocales=vocales + palabra[i] + ","
    else:
        consonantes= consonantes + palabra[i] + ","
print("las vocales de la palabra", palabra, "son", vocales)
print("las consonantes de la palabra", palabra, "son", consonantes)
=======
# Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:
palabra=input("introduce una palabra: ")
vocal=""
consonante=""
for i in range(0, len(palabra)):
    if palabra[i] in ["a", "e", "i", "o", "u"]:
        vocal= vocal + palabra[i]
    else:
        consonante= consonante + palabra[i]
print("las vocales de la palabra", palabra, "son", vocal)
print("las consonates de la palabra", palabra, "son", consonante)
>>>>>>> Stashed changes
