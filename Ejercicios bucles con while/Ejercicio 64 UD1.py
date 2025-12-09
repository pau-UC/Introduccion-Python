# Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas: a) total de pares b) total de impares c) total de números positivos d) total de números negativose) total de ceros f) total de la suma de todos los números introducidos.
numero=int(input("Introduce un número: "))
pares=0
impares=0
infinito=0
positivo=0
negativos=0
while infinito==0:
        if numero==-99:
            break
        if numero%2==0:
            pares+=1
        else:
            impares+=1
        if numero>0:
            positivo+=1
        else:
            negativos+=1
        if not numero==-99:
            numero=int(input("Introduce un número: "))
print("RESUMEN")
print("El número de pares es", pares)
print("El número de impares es", impares)
print("El número de positivos es", positivo)
print("El número de negativos es", negativos)