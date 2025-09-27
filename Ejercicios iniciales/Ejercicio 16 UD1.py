# Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso (raíz y división).
import math
var1=float(input("introduce un número: "))
raiz=math.sqrt(var1)
division=raiz/2
print("El resultado de la raíz es ", raiz)
print("El resultado de la division es ", division)