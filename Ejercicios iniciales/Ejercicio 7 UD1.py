#programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?
var1=int(input("introduce un número: "))
var2=int(input("introduce otro numero: "))
suma=var1+var2
resta=var1-var2
multiplicación=var1*var2
division=var1/var2
exponente=var1**var2
módulo=var1%var2
División_entera=var1//var2
print("la suma de las variables es", suma)
print("la resta de las variables es", resta)
print("la multiplicación de las variables es", multiplicación)
print("la division de las variables es", round(division, 2))
print("el exponente de las variables es", exponente)
print("el modulo de las variables es", módulo)