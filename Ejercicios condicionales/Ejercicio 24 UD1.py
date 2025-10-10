# Corrige los errores del siguiente código y comprueba que se ejecuta correctamente
var1=float(input("introduce el peso: "))
var2=float(input("introduce la altura"))
var_imc=var1/var2**2
print(f"Si pesas {var1} kilos y mides {var2}, tu IMC es:", var_imc)
if var_imc>= 25:
    print("hay sobrepeso")
else:
    print("Estás dentro de los parámetros normales")