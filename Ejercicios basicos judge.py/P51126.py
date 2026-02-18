intervals=input()
lista=[]
lista=intervals.split()
a1=lista[0]
b1=lista[1]
a2=lista[2]
b2=lista[3]
comprobación1=max(a1,a2)
comprobación2=min(b1,b2)
if comprobación2>=comprobación1:
    print(f"[{comprobación1},{comprobación2}]")
else:
    print("[]")