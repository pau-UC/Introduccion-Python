import math
numero=float(input())
num_inf=math.floor(numero)
num_sup=math.ceil(numero)
# por si es 0.5 que redondee para ariba para asegurarse
redondeo=round(numero)
print(num_inf, num_sup, redondeo)