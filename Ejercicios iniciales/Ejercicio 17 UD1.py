# Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
peso=float(input("introduce tu peso en kilogramos por favor: "))
altura=float(input("introduce tu altura en metros"))
imc=peso/(altura**2)
if imc>= 25:
    print("usted tiene sobrepeso")
else:
    print("usted no tiene sobrepeso")
