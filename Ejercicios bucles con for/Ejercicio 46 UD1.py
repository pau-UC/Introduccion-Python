<<<<<<< Updated upstream
# A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción. 
palabra=input("introduce una palabra: ")
vocales=""
consonantes=""
for i in range(len(palabra)):
    if palabra[i] in ["a", "e", "i", "o", "u"]:
        vocales=vocales + palabra[i] + ","
    elif palabra[i] in ["A", "E", "I", "O", "U"]:
        vocales=vocales + palabra[i] + ","
    else:
        consonantes= consonantes + palabra[i] + ","
print("las vocales de la palabra", palabra, "son", vocales)
print("las consonantes de la palabra", palabra, "son", consonantes)
=======
# A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
palabra=input("introduce una palabra: ")
vocal=""
consonante=""
for i in range(0, len(palabra)):
    if palabra[i] in ["a", "e", "i", "o", "u"]:
        vocal= vocal + palabra[i]
    elif palabra[i] in ["A", "E", "I", "O", "U"]:
        vocal= vocal + palabra[i]
    else:
        consonante= consonante + palabra[i]
print("las vocales de la palabra", palabra, "son", vocal)
print("las consonates de la palabra", palabra, "son", consonante)
>>>>>>> Stashed changes
