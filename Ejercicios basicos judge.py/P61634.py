año=int(input())
if año>=1800 and año<=9999:
    if (año%4==0 and año%100!=0) or año%400==0:
        print("YES")
    else:
        print("NO")