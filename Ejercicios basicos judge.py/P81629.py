import math
dinero=input()
lista=[]
lista=dinero.split()
for i in range(len(lista)):
    lista[i] = int(lista[i])
billete500=math.floor(lista[0]/500)
dinero1=lista[0]-500*billete500
billete200=math.floor(dinero1/200)
dinero2=dinero1-200*billete200
billete100=math.floor(dinero2/100)
dinero3=dinero2-100*billete100
billete50=math.floor(dinero3/50)
dinero4=dinero3-50*billete50
billete20=math.floor(dinero4/20)
dinero5=dinero4-20*billete20
billete10=math.floor(dinero5/10)
dinero6=dinero5-10*billete10
billete5=math.floor(dinero6/5)
dinero7=dinero6-5*billete5
moneda2=math.floor(dinero7/2)
dinero8=dinero7-2*moneda2
moneda1=math.floor(dinero8/1)
dinero9=dinero8-1*moneda1
cent50=math.floor(lista[1]/50)
dinero10=lista[1]-50*cent50
cent20=math.floor(dinero10/20)
dinero11=dinero10-20*cent20
cent10=math.floor(dinero11/10)
dinero12=dinero11-10*cent10
cent5=math.floor(dinero12/5)
dinero13=dinero12-5*cent5
cent2=math.floor(dinero13/2)
dinero14=dinero13-2*cent2
cent=dinero14
print("Banknotes of 500 euros:", billete500)
print("Banknotes of 200 euros:", billete200)
print("Banknotes of 100 euros:", billete100)
print("Banknotes of 50 euros:", billete50)
print("Banknotes of 20 euros:", billete20)
print("Banknotes of 10 euros:", billete10)
print("Banknotes of 5 euros:", billete5)
print("Coins of 2 euros:", moneda2)
print("Coins of 1 euro:", moneda1)
print("Coins of 50 cents:", cent50)
print("Coins of 20 cents:", cent20)
print("Coins of 10 cents:", cent10)
print("Coins of 5 cents:", cent5)
print("Coins of 2 cents:", cent2)
print("Coins of 1 cent:", cent)