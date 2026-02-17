intervals=input()
lista=[]
lista=intervals.split()
a1=lista[0]
b1=lista[1]
a2=lista[2]
b2=lista[3]
if a1==a2 and b1==b2:
    print("=")
elif a1>=a2 and b2>=b1:
    print("1")
elif a1<=a2 and b2<=b1:
    print("2")
else:
    print("?")