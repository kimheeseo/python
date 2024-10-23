a,b=map(int,input().split())
c=int(input())

if (b+c)>=60:
    d=(b+c)//60
    if (a+d) >= 24:
        e=a+d-24
    else:
        e=a+d             
    print(e, ((b+c)-60*d))

else:
    d=b+c
    print(a,int(d))