a=input()
listaA=a.split()
if len(listaA)==1:
    b=input()
    if b.isnumeric() and int(b)>0:
        listaA.append(b)
for i in range(len(listaA)):
    if i==0:
        a=int(listaA[i])
    if i==1:
        b=int(listaA[i])
if not b==0:
    resultado=a//b
    r=a%b
print(resultado, r)