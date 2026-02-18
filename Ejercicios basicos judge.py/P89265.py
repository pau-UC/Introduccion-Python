intervals=input()
lista=[]
lista=intervals.split()
a1=lista[0]
b1=lista[1]
a2=lista[2]
b2=lista[3]
comprobación1=max(a1,a2)
comprobación2=min(b1,b2)
igual=""
uno=""
dos=""
otro=""
if a1==a2 and b1==b2:
    igual="="
elif a1>=a2 and b2>=b1:
    uno="1"
elif a1<=a2 and b2<=b1:
    dos="2"
else:
    otro="?"
if comprobación2>=comprobación1 and igual=="=":
    print(f"{igual} , [{comprobación1},{comprobación2}]")
elif comprobación2>=comprobación1 and uno=="1":
    print(f"{uno} , [{comprobación1},{comprobación2}]")
elif comprobación2>=comprobación1 and dos=="2":
    print(f"{dos} , [{comprobación1},{comprobación2}]")
elif comprobación2>=comprobación1 and otro=="?":
    print(f"{otro} , [{comprobación1},{comprobación2}]")
elif comprobación2<comprobación1 and igual=="=":
    print("= , []")
elif comprobación2<comprobación1 and uno=="1":
    print("1 , []")
elif comprobación2<comprobación1 and dos=="2":
    print("2 , []")
elif comprobación2<comprobación1 and otro=="?":
    print("? , []")
else:
    print("[]")