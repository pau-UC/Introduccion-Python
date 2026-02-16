import math
segundos=int(input())
horas=0
minutos=0
segundos_finales=0
if segundos>=3600:
    horas=math.floor(segundos/3600)
    seg_restantes1=segundos-3600*horas
    minutos=math.floor(seg_restantes1/60)
    segundos_finales=seg_restantes1-60*minutos
    print(horas, minutos, segundos_finales)
elif segundos>=60:
    minutos=math.floor(segundos/60)
    segundos_finales=segundos-60*minutos
    print(horas, minutos, segundos_finales)
else:
    print(horas, minutos, segundos)