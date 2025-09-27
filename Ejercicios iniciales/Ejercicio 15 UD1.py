# Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
radio=float(input("introduce el radio del cilindro: "))
altura=float(input("introduce la altura deel cilindro: "))
area=2*math.pi*radio*(radio+altura)
perimetro=2*math.pi*radio
print("el perimetro del cilindro es", round(perimetro, 2))
print("el area del cilindro es", round(area, 2))