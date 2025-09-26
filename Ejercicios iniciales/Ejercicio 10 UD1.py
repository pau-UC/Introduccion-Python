# Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
dividendo=float(input("introduce el dividendo por favor: "))
divisor=float(input("introduce el divisor por favor: "))
cociente= dividendo/divisor
resto= dividendo%divisor
print("el cociente es", cociente)
print("el resto es", resto)
if dividendo%divisor==0:
    print("el dividendo es par")
else:   
    print("el dividendo es impar")