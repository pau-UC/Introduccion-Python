# Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo
import math
a=float(input("introduce el número con x sin elevar al quadrado: "))
b=float(input("introduce el número donde la x esta elevada al quadrado: "))
c=float(input("introduce el número sin x: "))
discriminante= b**2 - 4*a*c
if discriminante>0:
    x1=(-b + math.sqrt(discriminante)) / (2*a)
    x2=(-b - math.sqrt(discriminante)) / (2*a)
    print("el valor de x1 es", x1)
    print("el valor de x2 es", x2)
elif discriminante==0:
    x=-b / (2*a)
    print("el  valor de x es", x)
else:
    print("La raíz no puede ser un valor negativo")