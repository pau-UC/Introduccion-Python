# Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math
<<<<<<< HEAD
radio=float(input("introduce el radio del circulo: "))
perímetro=2*radio*math.pi
área=math.pi*radio**2 
print("El perímetro del círculo es", round(perímetro,1))
print("El área del círculo es", round(área,1))
=======
diametro=float(input("introduce el diametro del circulo"))
radio=diametro/2
area= math.pi*radio**2
perimetro=2*math.pi*radio
print("el perímetro del circulo es", round(perimetro, 1))
print("el area del circulo es", round(area, 1))
>>>>>>> 8bc9e8556587750bdc840bd96405b07d67e47087
