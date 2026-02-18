import math
numero=float(input())
num_inf=math.floor(numero)
num_sup=math.ceil(numero)
# que siempre que sea 0.5 redondee para ariba
redondeo=math.floor(numero+0.5)
print(num_inf, num_sup, redondeo)